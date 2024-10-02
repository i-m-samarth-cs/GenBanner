document.getElementById('videoForm').addEventListener('submit', function(event) {
    event.preventDefault();

    const directories = document.getElementById('directories').value.split(',');
    const num_banners = document.getElementById('num_banners').value;
    const fps = document.getElementById('fps').value;

    fetch('/generate-video', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            directories: directories,
            num_banners: num_banners,
            fps: fps
        })
    })
    .then(response => response.json())
    .then(data => {
        const output = document.getElementById('output');
        const video = document.getElementById('promoVideo');
        output.style.display = 'block';
        video.src = data.video_url;
    });
});
