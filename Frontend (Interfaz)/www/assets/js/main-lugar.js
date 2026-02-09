(function(){
  'use strict';
  const HT = window.HexaTour;
  const $ = s => document.querySelector(s);

  document.addEventListener('DOMContentLoaded', ()=>{
    const url = new URL(location.href);
    const cat = url.searchParams.get('cat') || '';
    $('#title').textContent = cat || 'Lugar';

    const opts = $('#opts');
    const detail = $('#detail');
    const img = $('#detailImg');
    const routeImg = $('#routeImg');
    const desc = $('#desc');
    const tPie = $('#tPie');
    const tVeh = $('#tVeh');
    const hOpen = $('#hOpen');
    const hClose = $('#hClose');
    const alertEl = $('#alert');
    const printBtn = $('#printBtn');
    const printRow = $('#printRow');
    const routeBtn = $('#routeBtn');
    const emgMsg = $('#emgMsg');
    let current = null;

    async function renderOptions(){
      opts.innerHTML = '';
      emgMsg.hidden = true;
      emgMsg.textContent = 'ALERTA ENVIADA!';

      if(cat === 'Urgencia'){
        detail.hidden = true;
        ['Carabineros','Ambulancia','Bomberos'].forEach(n=>{
          const b = document.createElement('button');
          b.className = 'opt urg ' + (n==='Carabineros'?'carabineros':n==='Ambulancia'?'ambulancia':'bomberos');
          b.type = 'button';
          b.textContent = n;
          b.onclick = ()=>{ if(confirm('¿Está seguro de llamar a ' + n + '?')){ emgMsg.hidden = false; } };
          opts.appendChild(b);
        });
        return;
      }

      const folder = HT.catFolder(cat || 'Restaurantes');
      const items = await HT.loadCategoryList(folder);
      if(!items.length){
        const msg = document.createElement('div');
        msg.textContent = 'No hay datos cargados para esta categoria.';
        opts.appendChild(msg);
        detail.hidden = true;
        return;
      }

      items.forEach(item=>{
        const b = document.createElement('button');
        b.className = 'opt';
        b.type = 'button';
        b.textContent = item.name || item.slug || 'Lugar';
        b.onclick = ()=>{ selectPlace(item.slug, item.name || item.slug); };
        opts.appendChild(b);
      });

      detail.hidden = true;
    }

    async function selectPlace(slug, name){
      const folder = HT.catFolder(cat || 'Restaurantes');
      current = {cat:cat, folder:folder, name:name, slug:slug};

      img.onerror = ()=>{ img.style.display = 'none'; };
      img.src = HT.resolveAssetPath('img/' + folder + '/' + slug + '.jpg');
      img.alt = 'Imagen de ' + name;
      img.style.display = 'block';

      routeImg.style.display = 'none';
      routeImg.removeAttribute('src');

      desc.textContent = '—';
      tPie.textContent = '—';
      tVeh.textContent = '—';
      hOpen.textContent = '—';
      hClose.textContent = '—';
      alertEl.textContent = '—';

      printRow.style.display = 'none';
      printBtn.disabled = true;
      printBtn.setAttribute('aria-disabled','true');

      const poi = await HT.loadPoi(folder, slug);
      if(!poi){
        desc.textContent = 'Metadatos no encontrados.';
      } else {
        current.poi = poi;
        HT.fillPoiFields(poi.fields, {desc:desc, tPie:tPie, tVeh:tVeh, hOpen:hOpen, hClose:hClose, alertEl:alertEl});

        const mainImg = (poi.images && poi.images.main) ? HT.resolveAssetPath(poi.images.main) : img.src;
        img.src = mainImg;
        if(poi.images && poi.images.route){
          current.routeImg = HT.resolveAssetPath(poi.images.route);
        } else {
          current.routeImg = HT.resolveAssetPath('img/' + folder + '/ruta' + slug + '.jpg');
        }

        const routeText = (poi.route && poi.route.text) ? poi.route.text.trim() : '';
        if(routeText){
          printRow.style.display = '';
          printBtn.disabled = false;
          printBtn.setAttribute('aria-disabled','false');
        }
      }

      detail.hidden = false;
    }

    routeBtn.addEventListener('click', ()=>{
      if(!current) return;
      routeImg.onload = ()=>{ routeImg.style.display = 'block'; };
      routeImg.onerror = ()=>{ routeImg.style.display = 'none'; alert('No se encontró la imagen de ruta.'); };
      routeImg.removeAttribute('loading');
      routeImg.setAttribute('loading','eager');
      routeImg.decoding = 'async';
      routeImg.src = current.routeImg || HT.resolveAssetPath('img/' + current.folder + '/ruta' + current.slug + '.jpg');
      routeImg.alt = 'Ruta hacia ' + current.name;
    });

    printBtn.addEventListener('click', async ()=>{
      if(!current) return;
      const file = current.folder + '/' + current.slug;
      try{
        const r = await fetch('../api/print-ruta?name=' + encodeURIComponent(current.name) + '&cat=' + encodeURIComponent(current.folder) + '&slug=' + encodeURIComponent(current.slug) + '&file=' + encodeURIComponent(file), {cache:'no-store'});
        if(!r.ok) throw 0;
        alert('Indicaciones enviadas a impresión.');
      }catch(e){
        alert('No se pudo enviar a impresión (verifique la BD en /www/db/).');
      }
    });

    renderOptions();
  });
})();
