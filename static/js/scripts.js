// 脚本文件：static/js/scripts.js
document.addEventListener('DOMContentLoaded', function() {
    console.log('JavaScript is working!');

    // 为下载按钮添加点击事件
    document.querySelectorAll('.btn-download').forEach(button => {
        button.addEventListener('click', function(event) {
            event.preventDefault();
            const href = this.getAttribute('href');
            const filename = this.getAttribute('download');
            const a = document.createElement('a');
            a.href = href;
            a.download = filename;
            document.body.appendChild(a);
            a.click();
            document.body.removeChild(a);
        });
    });

    // 为播放按钮添加点击事件
    document.querySelector('.btn-play-video').addEventListener('click', function() {
        const videoUrl = document.querySelector('.card-aside-column').getAttribute('data-video-url');
        const videoPlayer = document.createElement('video');
        videoPlayer.src = videoUrl;
        videoPlayer.controls = true;
        videoPlayer.style.width = '100%';
        videoPlayer.style.height = 'auto';
        document.querySelector('.card-aside-column').innerHTML = '';
        document.querySelector('.card-aside-column').appendChild(videoPlayer);
    });
});