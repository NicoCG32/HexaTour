(function(){
  'use strict';
  const HT = window.HexaTour;
  const $ = s => document.querySelector(s);

  const HEXATOUR_PUNTO = 'PUNTO_HEXATOUR_AQUI';

  function buildSmsBodyUrgencia(tipo){
    return [
      'ALERTA URGENCIA HEXATOUR',
      'Punto: ' + HEXATOUR_PUNTO,
      'Servicio requerido: ' + tipo,
      'Urgencia: [describa brevemente]',
      'Se necesita con urgencia: [indique lo que requiere]'
    ].join('\n');
  }

  document.addEventListener('DOMContentLoaded', ()=>{
    const url = new URL(location.href);
    const cat = url.searchParams.get('cat') || '';
    $('#title').textContent = cat || 'Selecciona una categoría';

    const opts = $('#opts');
    const detailCard = $('#detailCard');
    const img = $('#detailImg');
    const routeImg = $('#routeImg');
    const desc = $('#desc');
    const tPie = $('#tPie');
    const tVeh = $('#tVeh');
    const hOpen = $('#hOpen');
    const hClose = $('#hClose');
    const alertEl = $('#alert');
    const routeBtn = $('#routeBtn');
    const downloadBtn = $('#downloadBtn');
    const emgMsg = $('#emgMsg');
    let current = null;

    async function renderOpts(){
      opts.innerHTML = '';
      emgMsg.hidden = true;
      emgMsg.textContent = 'ALERTA ENVIADA!';

      if(cat === 'Urgencia'){
        ['Carabineros','Ambulancia','Bomberos'].forEach(n=>{
          const b = document.createElement('button');
          b.className = 'opt urg ' + (n==='Carabineros'?'carabineros':n==='Ambulancia'?'ambulancia':'bomberos');
          b.type = 'button';
          b.textContent = n;
          b.onclick = ()=>{
            if(confirm('¿Está seguro de contactar a ' + n + ' por SMS?')){
              const phone = '+56935774427';
              const body = buildSmsBodyUrgencia(n);
              const smsUrl = 'sms:' + phone + '?body=' + encodeURIComponent(body);
              emgMsg.hidden = false;
              emgMsg.textContent = 'Abriendo app de mensajes...';
              location.href = smsUrl;
            }
          };
          opts.appendChild(b);
        });
        detailCard.hidden = true;
        return;
      }

      const base = HT.labelBase(cat || 'Restaurantes');
      const folder = HT.catFolder(cat || 'Restaurantes');
      const col = {
        'Restaurantes':'#c2410c','Hospedajes':'#1d4ed8','Plazas':'#16a34a','Ríos':'#0d9488','Pisqueras':'#b45309','Campings':'#047857','Ferias Artesanales':'#7c3aed','Servicios':'#374151','Universidad':'#0284c7'
      }[cat] || '#0f172a';
      document.documentElement.style.setProperty('--opt-bg', col);

      const items = await HT.loadCategoryList(folder);
      if(!items.length){
        const msg = document.createElement('div');
        msg.textContent = 'No hay datos cargados para esta categoria.';
        opts.appendChild(msg);
        detailCard.hidden = true;
        return;
      }

      items.forEach(item=>{
        const btn = document.createElement('button');
        btn.className = 'opt';
        btn.type = 'button';
        btn.textContent = item.name || item.slug || (base + '');
        btn.onclick = ()=>{ selectPlace(item.slug, item.name || item.slug); };
        opts.appendChild(btn);
      });

      detailCard.hidden = true;
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
      downloadBtn.hidden = true;

      desc.textContent = '—';
      tPie.textContent = '—';
      tVeh.textContent = '—';
      hOpen.textContent = '—';
      hClose.textContent = '—';
      alertEl.textContent = '—';

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
        downloadBtn.hidden = !routeText;
      }

      detailCard.hidden = false;
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
      routeImg.removeAttribute('sizes');
      routeImg.removeAttribute('srcset');
    });

    downloadBtn.addEventListener('click', ()=>{
      if(!current) return;
      const file = current.folder + '/' + current.slug;
      const url = '../api/route-pdf?name=' + encodeURIComponent(current.name) + '&cat=' + encodeURIComponent(current.folder) + '&slug=' + encodeURIComponent(current.slug) + '&file=' + encodeURIComponent(file) + '&dl=1';
      location.href = url;
    });

    renderOpts();
  });
})();
