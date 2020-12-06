"use strict";

//entry point :
function main(){
    THREE.JeelizHelper.init({
      canvasThreeId: 'webojiCanvas',
      canvasId: 'jeefacetransferCanvas',

      assetsParentPath: 'assets/3D/',
      NNCpath: 'dist/',

      //RACCOON:
      meshURL: 'assets/3D/meshes/fox.json',
      matParameters: {
        diffuseMapURL: 'assets/3D/textures/Fox_albedo.png',
        specularMapURL: 'assets/3D/textures/Fox_specular.png',
        flexMapURL: 'assets/3D/textures/Fox_flex.png'
      },
      
      position: [0,-80,0],
      scale: 1.2
    });
} //end main()
