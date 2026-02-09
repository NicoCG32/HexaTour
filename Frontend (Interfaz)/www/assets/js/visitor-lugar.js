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
      const baseSlug = HT.slugify(base);
      const col = {
        'Restaurantes':'#c2410c','Hospedajes':'#1d4ed8','Plazas':'#16a34a','Ríos':'#0d9488','Pisqueras':'#b45309','Campings':'#047857','Ferias Artesanales':'#7c3aed','Servicios':'#374151','Universidad':'#0284c7'
      }[cat] || '#0f172a';
      document.documentElement.style.setProperty('--opt-bg', col);

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
              const btn = document.createElement('button');
              btn.className = 'opt';
              btn.type = 'button';
              btn.textContent = displayName;
              btn.onclick = ()=>{ selectPlace(slug, displayName); };
              opts.appendChild(btn);
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

      detailCard.hidden = true;
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
      downloadBtn.hidden = true;

      desc.textContent = '—';
      tPie.textContent = '—';
      tVeh.textContent = '—';
      hOpen.textContent = '—';
      hClose.textContent = '—';
      alertEl.textContent = '—';

      const canDownload = await hasRouteFile(folder, slug);
      downloadBtn.hidden = !canDownload;

      HT.loadMeta(current, {desc:desc, tPie:tPie, tVeh:tVeh, hOpen:hOpen, hClose:hClose, alertEl:alertEl});

      detailCard.hidden = false;
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
      routeImg.setAttribute('sizes', '(max-width: 768px) 90vw, 720px');
      routeImg.setAttribute('srcset', '../img/' + current.folder + '/ruta' + current.slug + '-640.jpg 640w, ../img/' + current.folder + '/ruta' + current.slug + '-1280.jpg 1280w');
    });

    downloadBtn.addEventListener('click', ()=>{
      if(!current) return;
      const file = current.folder + '/indicaciones' + current.slug + 'ruta.txt';
      const url = '../api/route-pdf?name=' + encodeURIComponent(current.name) + '&file=' + encodeURIComponent(file) + '&dl=1';
      location.href = url;
    });

    renderOpts();
  });
})();
