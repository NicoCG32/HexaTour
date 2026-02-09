(function(){
  'use strict';
  const HT = window.HexaTour;
  const $ = s => document.querySelector(s);

  async function hasRouteFile(folder, slug){
    const path = '../rutas/' + folder + '/indicaciones' + slug + 'ruta.txt';
    try{
      const r = await fetch(path, {cache:'no-store'});
      return r.ok;
    }catch(e){
      return false;
    }
  }

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

      const base = HT.labelBase(cat || 'Restaurantes');
      const folder = HT.catFolder(cat || 'Restaurantes');
      const baseSlug = HT.slugify(base);
      let used = false;
      let nameMap = {};

      try{
        const rn = await fetch('../datos/' + folder + '/nombres.txt', {cache:'no-store'});
        if(rn.ok){
          const txt = await rn.text();
          txt.split(/\r?\n+/).forEach(line=>{
            const l = line.trim();
            if(!l || l.startsWith('#')) return;
            const parts = l.split('|');
            const id = (parts[0]||'').trim();
            const label = (parts[1]||'').trim();
            if(id && label){ nameMap[id] = label; }
          });
        }
      }catch(e){}

      try{
        const r = await fetch('../datos/' + folder + '/_index.txt', {cache:'no-store'});
        if(r.ok){
          const lines = (await r.text()).split(/\r?\n+/).map(s=>s.trim()).filter(s=>s && !s.startsWith('#'));
          if(lines.length){
            lines.forEach(slug=>{
              const suf = slug.startsWith(baseSlug) ? slug.slice(baseSlug.length) : slug;
              const fallbackName = base + ' ' + suf.toUpperCase();
              const displayName = nameMap[slug] || fallbackName;
              const b = document.createElement('button');
              b.className = 'opt';
              b.type = 'button';
              b.textContent = displayName;
              b.onclick = ()=>{ selectPlace(slug, displayName); };
              opts.appendChild(b);
            });
            used = true;
          }
        }
      }catch(e){}

      if(!used){
        'ABCDEFGHIJKLMNOPQRSTUVWXYZ'.split('').forEach(suf=>{
          const name = base + ' ' + suf;
          const slug = HT.slugify(name);
          const testSrc = '../img/' + folder + '/' + slug + '.jpg';
          const b = document.createElement('button');
          b.className = 'opt';
          b.type = 'button';
          b.textContent = name;
          b.style.display = 'none';
          b.onclick = ()=>{ selectPlace(slug, name); };
          opts.appendChild(b);
          const probe = new Image();
          probe.onload = ()=>{ b.style.display = ''; };
          probe.onerror = ()=>{ b.remove(); };
          probe.src = testSrc;
        });
      }

      detail.hidden = true;
    }

    async function selectPlace(slug, name){
      const folder = HT.catFolder(cat || 'Restaurantes');
      current = {cat:cat, folder:folder, name:name, slug:slug};

      img.onerror = ()=>{ img.style.display = 'none'; };
      img.src = '../img/' + folder + '/' + slug + '.jpg';
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
      const canPrint = await hasRouteFile(folder, slug);
      if(canPrint){
        printRow.style.display = '';
        printBtn.disabled = false;
        printBtn.setAttribute('aria-disabled','false');
      }

      HT.loadMeta(current, {desc:desc, tPie:tPie, tVeh:tVeh, hOpen:hOpen, hClose:hClose, alertEl:alertEl});

      detail.hidden = false;
    }

    routeBtn.addEventListener('click', ()=>{
      if(!current) return;
      routeImg.onload = ()=>{ routeImg.style.display = 'block'; };
      routeImg.onerror = ()=>{ routeImg.style.display = 'none'; alert('No se encontró la imagen de ruta.'); };
      routeImg.removeAttribute('loading');
      routeImg.setAttribute('loading','eager');
      routeImg.decoding = 'async';
      routeImg.src = '../img/' + current.folder + '/ruta' + current.slug + '.jpg';
      routeImg.alt = 'Ruta hacia ' + current.name;
    });

    printBtn.addEventListener('click', async ()=>{
      if(!current) return;
      const file = current.folder + '/indicaciones' + current.slug + 'ruta.txt';
      try{
        const r = await fetch('../api/print-ruta?name=' + encodeURIComponent(current.name) + '&file=' + encodeURIComponent(file), {cache:'no-store'});
        if(!r.ok) throw 0;
        alert('Indicaciones enviadas a impresión.');
      }catch(e){
        alert('No se pudo enviar a impresión (verifique /www/rutas/).');
      }
    });

    renderOptions();
  });
})();
