(function(){
  'use strict';

  const isDemo = document.querySelector('meta[name="hexatour-mode"]')?.content === 'demo'
    || new URL(location.href).searchParams.get('demo') === '1';
  const siteRoot = new URL('../../', document.currentScript.src);

  function siteUrl(path){
    return new URL(path, siteRoot).href;
  }

  function withMode(path){
    const url = new URL(path, location.href);
    if(isDemo) url.searchParams.set('demo', '1');
    return url.href;
  }

  function showDemoMessage(text, container){
    let message = container.querySelector('.demo-message');
    if(!message){
      message = document.createElement('p');
      message.className = 'demo-message';
      message.setAttribute('role', 'status');
      container.appendChild(message);
    }
    message.textContent = text;
  }

  document.addEventListener('DOMContentLoaded', ()=>{
    if(!isDemo) return;
    const banner = document.createElement('aside');
    banner.className = 'demo-banner';
    banner.setAttribute('aria-label', 'Modo demo');
    const title = document.createElement('strong');
    title.textContent = 'Demo sin hardware';
    const description = document.createElement('p');
    description.textContent = 'Datos de ejemplo: horarios, tiempos y rutas no verificados. No usar para orientación ni atención de urgencias. Impresión simulada, PDF no disponible y urgencias sin envío.';
    const nav = document.createElement('nav');
    nav.setAttribute('aria-label', 'Vistas de la demo');
    [['Visitante', 'visitor/'], ['Operador', 'main/']].forEach(([label, path])=>{
      const link = document.createElement('a');
      link.textContent = label;
      link.href = withMode(siteUrl(path));
      nav.appendChild(link);
    });
    banner.append(title, description, nav);
    document.body.prepend(banner);
  });

  function normalize(s){
    return (s||'').toLowerCase().normalize('NFD').replace(/[\u0300-\u036f]/g,'').replace(/ñ/g,'n');
  }

  function placeLabel(item, index, items){
    const name = item.name || item.slug || 'Lugar';
    const repeated = items.filter(other=>(other.name || other.slug || 'Lugar') === name).length > 1;
    return isDemo && repeated ? name + ' (ejemplo ' + (index + 1) + ')' : name;
  }

  function catFolder(cat){
    switch(cat){
      case 'Restaurantes': return 'restaurantes';
      case 'Hospedajes': return 'hospedajes';
      case 'Plazas': return 'plazas';
      case 'Ríos': return 'rios';
      case 'Pisqueras': return 'pisqueras';
      case 'Campings': return 'campings';
      case 'Ferias Artesanales': return 'ferias';
      case 'Servicios': return 'servicios';
      case 'Universidad': return 'universidad';
      case 'Urgencia': return 'urgencias';
      default: return 'otros';
    }
  }

  function labelBase(cat){
    switch(cat){
      case 'Restaurantes': return 'Restaurante';
      case 'Hospedajes': return 'Hospedaje';
      case 'Plazas': return 'Plaza';
      case 'Ríos': return 'Río';
      case 'Pisqueras': return 'Pisquera';
      case 'Campings': return 'Camping';
      case 'Ferias Artesanales': return 'Feria';
      case 'Servicios': return 'Servicio';
      case 'Universidad': return 'Universidad';
      case 'Urgencia': return 'Urgencia';
      default: return 'Lugar';
    }
  }

  function slugify(s){
    return normalize(s).replace(/[^a-z0-9]+/g,'').trim();
  }

  async function fetchTextCandidates(candidates){
    for(const url of candidates){
      try{
        const r = await fetch(url, {cache:'no-store'});
        if(r.ok){
          return await r.text();
        }
      }catch(e){}
    }
    return null;
  }

  function resolveAssetPath(path){
    if(!path) return '';
    if(path.startsWith('/')) return path;
    return '../' + path.replace(/^\.\//, '');
  }

  async function loadCategoryList(category){
    const candidates = [
      '../db/categories/' + category + '.json',
      '/db/categories/' + category + '.json',
      '/www/db/categories/' + category + '.json',
      '../../db/categories/' + category + '.json',
      'db/categories/' + category + '.json'
    ];
    const text = await fetchTextCandidates(candidates);
    if(!text) return [];
    try{
      const data = JSON.parse(text);
      return Array.isArray(data.items) ? data.items : [];
    }catch(e){
      return [];
    }
  }

  async function loadPoi(category, slug){
    const p = category + '/' + slug + '.json';
    const candidates = [
      '../db/poi/' + p,
      '/db/poi/' + p,
      '/www/db/poi/' + p,
      '../../db/poi/' + p,
      'db/poi/' + p
    ];
    const text = await fetchTextCandidates(candidates);
    if(!text) return null;
    try{
      return JSON.parse(text);
    }catch(e){
      return null;
    }
  }

  function fillPoiFields(fields, targets){
    const safe = (fields || {});
    targets.desc.textContent = safe.descripcion || '—';
    targets.tPie.textContent = safe.tpie || '—';
    targets.tVeh.textContent = safe.tveh || '—';
    targets.hOpen.textContent = safe.apertura || '—';
    targets.hClose.textContent = safe.cierre || '—';
    targets.alertEl.textContent = safe.alertas || '—';
  }

  window.HexaTour = {
    isDemo,
    siteUrl,
    withMode,
    showDemoMessage,
    placeLabel,
    normalize,
    catFolder,
    labelBase,
    slugify,
    resolveAssetPath,
    loadCategoryList,
    loadPoi,
    fillPoiFields
  };
})();
