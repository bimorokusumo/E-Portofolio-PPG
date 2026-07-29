import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Remove the Spotify widget
spotify_regex = r'<!-- Floating Spotify Player for BGM -->.*?<\/script>'
text = re.sub(spotify_regex, '', text, flags=re.DOTALL)

youtube_bgm = """
<!-- YouTube BGM Player -->
<div id="yt-bgm-container" style="position: fixed; bottom: 20px; right: 20px; z-index: 9999; background: white; padding: 10px 20px; border-radius: 50px; box-shadow: 0 10px 25px rgba(0,0,0,0.15); display: flex; align-items: center; gap: 10px; cursor: pointer; border: 1px solid #e2e8f0; transition: all 0.3s ease;" onclick="toggleBGM()" onmouseover="this.style.transform='scale(1.05)'" onmouseout="this.style.transform='scale(1)'">
    <div id="bgm-icon" style="font-size: 1.2rem; animation: pulse-glow 2s infinite;">🎵</div>
    <div style="font-weight: 600; color: #475569; font-size: 0.9rem;" id="bgm-text">BGM: Memuat...</div>
</div>

<div id="yt-player" style="position: absolute; width: 0; height: 0; overflow: hidden; left: -9999px;"></div>
<script src="https://www.youtube.com/iframe_api"></script>
<script>
    var bgmPlayer;
    var bgmState = 'loading'; // loading, playing, paused
    
    function onYouTubeIframeAPIReady() {
        bgmPlayer = new YT.Player('yt-player', {
            height: '0',
            width: '0',
            videoId: 'kPa7bsKwL-c', // Die With A Smile (Bruno Mars, Lady Gaga) - Hits Barat
            playerVars: {
                'autoplay': 0, // We will trigger play manually on interaction
                'loop': 1,
                'playlist': 'kPa7bsKwL-c',
                'controls': 0,
                'disablekb': 1
            },
            events: {
                'onReady': onPlayerReady,
                'onStateChange': onPlayerStateChange
            }
        });
    }

    function onPlayerReady(event) {
        document.getElementById('bgm-text').innerText = "BGM: Klik untuk Putar";
        document.getElementById('bgm-icon').style.animation = "none";
        bgmState = 'paused';
        
        // Autoplay on first click anywhere on the document
        const startAudio = function() {
            if(bgmState === 'paused') {
                bgmPlayer.playVideo();
                document.removeEventListener('click', startAudio);
            }
        };
        document.addEventListener('click', startAudio);
    }
    
    function onPlayerStateChange(event) {
        if (event.data == YT.PlayerState.PLAYING) {
            bgmState = 'playing';
            document.getElementById('bgm-text').innerText = "BGM: ON (Die With A Smile)";
            document.getElementById('bgm-icon').style.animation = "pulse-glow 2s infinite";
        } else if (event.data == YT.PlayerState.PAUSED || event.data == YT.PlayerState.ENDED) {
            bgmState = 'paused';
            document.getElementById('bgm-text').innerText = "BGM: OFF";
            document.getElementById('bgm-icon').style.animation = "none";
        }
    }

    function toggleBGM() {
        if (bgmState === 'playing') {
            bgmPlayer.pauseVideo();
        } else if (bgmState === 'paused') {
            bgmPlayer.playVideo();
        }
    }
</script>
"""

# ensure no duplicate insertion if run multiple times
if '<!-- YouTube BGM Player -->' not in text:
    text = text.replace('</body>', youtube_bgm + '\n</body>')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("YouTube BGM widget added.")
