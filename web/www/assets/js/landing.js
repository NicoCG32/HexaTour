(function(){
  'use strict';
  function go(){
    location.href = '/visitor/';
  }
  const btn = document.getElementById('go');
  if(btn) btn.onclick = go;
  setTimeout(go, 2000);
})();
