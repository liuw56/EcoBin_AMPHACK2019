// Configure a few settings and attach camera
Webcam.set({
    width: 320,
    height: 180,
    image_format: 'jpeg',
    jpeg_quality: 90
   });
   Webcam.attach( '#my_camera' );
  
  function take_snapshot() {
   // take snapshot and get image data
   Webcam.snap( function(data_uri) {
    // display results in page
    document.getElementById('results').innerHTML = '<img id="imageprev" src="'+data_uri+'"/>';
    } );
  }
  
  function saveSnap(){
   // Get base64 value from <img id='imageprev'> source
   var base64image = document.getElementById("imageprev").src;
  
   Webcam.upload( base64image, 'upload.php', function(code, text) {
    console.log('Save successfully');
    //console.log(text);
   });
  }