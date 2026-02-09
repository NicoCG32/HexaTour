(function(){
  'use strict';

  function normalize(s){
    return (s||'').toLowerCase().normalize('NFD').replace(/[\u0300-\u036f]/g,'').replace(/ñ/g,'n');
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
