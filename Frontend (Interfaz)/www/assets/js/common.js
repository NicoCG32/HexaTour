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

  async function loadMeta(current, targets){
    const p = current.folder + '/' + current.slug + '.txt';
    const candidates = [
      '../datos/' + p,
      '/datos/' + p,
      '/www/datos/' + p,
      '../../datos/' + p,
      'datos/' + p
    ];
    const text = await fetchTextCandidates(candidates);
    if(!text){
      targets.desc.textContent = 'Metadatos no encontrados.';
      return;
    }
    const cleanKey = s => (s||'').toLowerCase().normalize('NFD').replace(/[\u0300-\u036f]/g,'').replace(/ñ/g,'n').trim();
    const map = {};
    text.split(/\r?\n+/).forEach(line=>{
      if(!line || line.trim().startsWith('#')) return;
      const m = line.match(/^\s*([^=]+?)\s*=\s*(.*?)\s*$/);
      if(m){
        map[cleanKey(m[1])] = m[2];
      }
    });
    if(map['descripcion']) targets.desc.textContent = map['descripcion'];
    if(map['tpie']) targets.tPie.textContent = map['tpie'];
    if(map['tveh']) targets.tVeh.textContent = map['tveh'];
    if(map['apertura']) targets.hOpen.textContent = map['apertura'];
    if(map['cierre']) targets.hClose.textContent = map['cierre'];
    if(map['alertas']) targets.alertEl.textContent = map['alertas'];
  }

  window.HexaTour = {
    normalize,
    catFolder,
    labelBase,
    slugify,
    loadMeta
  };
})();
