var xmlHttp = createXmlHttpRequestObject();

function createXmlHttpRequestObject() {
	var xmlHttp;
	
	if(window.XMLHttpRequest) {
		try {
			xmlHttp = new XMLHttpRequest();
		} catch(e) {
			xmlHttp = false;
		}
	} else {
		try {
			xmlHttp = new ActiveXObject("Microsoft.XMLHTTP");
		} catch(e) {
			xmlHttp = false;
		}
	}
	
	if (!xmlHttp)
		alert("can't create xmlhttp object");
	else 
		return xmlHttp;
}

function process() {
	if (xmlHttp.readyState == 0 || xmlHttp.readyState == 4) {
		var food = encodeURIComponent(document.getElementById('userInput').value);
		xmlHttp.open("GET","foodstore.php?food="+food,true);
		xmlHttp.onreadystatechange = handleServerResponse;
		xmlHttp.send(null);
	}
	else {
		setTimeout('process()',1000);
	}
}

function handleServerResponse() {
	if (xmlHttp.readyState == 4) {
		if (xmlHttp.status == 200) {
			var xmlResponse = xmlHttp.responseXML;
			var xmlDocumentElement = xmlResponse.documentElement;
			var message = xmlDocumentElement.firstChild.data;
			document.getElementById('underInput').innerHTML = '<span style="color:blue">'+message+'</span>';
			//setTimeout('process()',1000);
		} else {
			alert('Server down!');
		}
	}
}