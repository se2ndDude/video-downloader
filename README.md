<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Universal Video Downloader</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background-color: #0f172a; /* Dark background */
            color: #e2e8f0;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            margin: 0;
        }
        .container {
            background-color: #1e293b;
            padding: 2rem;
            border-radius: 15px;
            box-shadow: 0 10px 25px rgba(0,0,0,0.5);
            width: 100%;
            max-width: 450px;
            text-align: center;
        }
        h1 { margin-bottom: 1.5rem; font-size: 1.5rem; color: #38bdf8; }
        .input-group { margin-bottom: 1.5rem; }
        input {
            width: 90%;
            padding: 12px;
            border-radius: 8px;
            border: 1px solid #334155;
            background-color: #0f172a;
            color: white;
            outline: none;
        }
        button {
            width: 100%;
            padding: 12px;
            border-radius: 8px;
            border: none;
            background-color: #3b82f6;
            color: white;
            font-weight: bold;
            cursor: pointer;
            transition: background 0.3s;
        }
        button:hover { background-color: #2563eb; }
        
        #result {
            display: none;
            margin-top: 20px;
            background: #0f172a;
            padding: 15px;
            border-radius: 10px;
        }
        img { max-width: 100%; border-radius: 8px; margin-bottom: 10px; }
        .download-btn {
            display: inline-block;
            text-decoration: none;
            background-color: #22c55e;
            color: white;
            padding: 10px 20px;
            border-radius: 5px;
            font-weight: bold;
        }
        .loader { display: none; margin: 10px auto; color: #94a3b8; }
    </style>
</head>
<body>

<div class="container">
    <h1>🚀 AI Video Downloader</h1>
    <p style="font-size: 0.9rem; color: #94a3b8;">Support: TikTok, Facebook, IG, dll.</p>
    
    <div class="input-group">
        <input type="text" id="urlInput" placeholder="Tempel Link TikTok/FB di sini...">
    </div>
    
    <button onclick="processVideo()">Gas Download!</button>
    <div class="loader" id="loader">Sedang mencari video...</div>

    <div id="result">
        <h3 id="vidTitle" style="font-size: 1rem;">Judul Video</h3>
        <img id="vidThumb" src="" alt="Thumbnail">
        <br>
        <a id="downloadLink" href="#" target="_blank" class="download-btn">Download Video</a>
    </div>
</div>

<script>
    async function processVideo() {
        const url = document.getElementById('urlInput').value;
        const resultDiv = document.getElementById('result');
        const loader = document.getElementById('loader');

        if(!url) return alert("Link kosong bro!");

        // Reset UI
        resultDiv.style.display = 'none';
        loader.style.display = 'block';

        try {
            const response = await fetch('/api/download', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ url: url })
            });
            
            const data = await response.json();
            
            if(data.success) {
                document.getElementById('vidTitle').innerText = data.title;
                document.getElementById('vidThumb').src = data.thumbnail;
                document.getElementById('downloadLink').href = data.url;
                resultDiv.style.display = 'block';
            } else {
                alert("Gagal: " + data.error);
            }
        } catch (err) {
            alert("Error server!");
        } finally {
            loader.style.display = 'none';
        }
    }
</script>

</body>
</html>
