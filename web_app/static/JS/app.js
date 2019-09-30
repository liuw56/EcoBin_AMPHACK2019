// Configure a few settings and attach camera
Webcam.set({
    width: 320,
    height: 180,
    image_format: 'jpeg',
    jpeg_quality: 90
   });
   Webcam.attach( '#my_camera' );
  var da;
  function take_snapshot() {
   // take snapshot and get image data
   Webcam.snap( function(data_uri) {
    da = data_uri;
    document.getElementById('results').innerHTML = '<img id="imageprev" src="'+data_uri+'"/>';

    // display results in page
    } );
    
  }

  function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
  };
  
  function saveSnap(){
   // Get base64 value from <img id='imageprev'> source
   var img_url = "http://localhost:9999/api";
   var formdData = new FormData();
   formdData.append("image",da);
  //  document.write(da)
   $.ajax({ 
     type: 'POST',
     contentType: false,
     processData: false,
     url: img_url,
     cache:false,
     data:formdData});
    //  window.location.replace("http://localhost:9999/pridict")
    //  (function relocate(){
    //   window.location.replace("http://localhost:9999/")
    // })();
  };

  // function goHomepage(){
  //   window.location.redirct("http://localhost:9999/")
  // };

  // function goCamera(){
  //   window.location.redirct("http://localhost:9999/cancel")
  // };

  // function goInfo(){
  //   window.location.redirct("http://localhost:9999/predict")
  // };

  

  // redirect= function relocate(){
  //   window.location.replace("http://localhost:9999/")
  // };