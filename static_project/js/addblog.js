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

	function upload_A()
	{
		var storage = firebase.storage();
		var file = document.getElementById("in2").files[0];
		var imageName = file.name;
		var storageRef = firebase.storage().ref('BlogPost/'+ imageName);
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

function upload_B()
	{
		var storage = firebase.storage();
		var file = document.getElementById("in2").files[0];
		var imageName = file.name;
		var storageRef = firebase.storage().ref('HelpPost/'+ imageName);
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