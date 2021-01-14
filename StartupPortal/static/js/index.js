var config = {
    "apiKey": "AIzaSyDFtg_YkT7Ej_sCf63gRudcgjTGhkUwthU",
    "authDomain": "startupcarvaan.firebaseapp.com",
    "databaseURL": "https://startupcarvaan.firebaseio.com",
    "projectId": "startupcarvaan",
    "storageBucket": "startupcarvaan.appspot.com",
    "messagingSenderId": "844859435167",
    "appId": "1:844859435167:web:921c1da84bcdf026c89aaa",
    "measurementId": "G-MHFP9HXHE5"
    };
    
    firebase.initializeApp(config);
	function upload()
	{
		var storage = firebase.storage();
		var file = document.getElementById("files").files[0];
		var imageName = file.name;
		var storageRef = firebase.storage().ref('Idea/'+ imageName);
		var thisref = storageRef.put(file);

		thisref.on('state_changed', function(snapshot){
			console.log("File uploaded successfully");
		},
		function(error){
			console.log(error.message);
		},

		function(){
        thisref.snapshot.ref.getDownloadURL().then(function(downloadURL){
			document.getElementById("url").value =  downloadURL;
		});
	});
}