with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

spotify_widget = """
<!-- Floating Spotify Player for BGM -->
<div id="spotify-bgm" style="position: fixed; bottom: 30px; right: 30px; z-index: 9999; width: 320px; box-shadow: 0 15px 35px rgba(0,0,0,0.2); border-radius: 14px; transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275); transform: translateY(0);">
    
    <!-- Header/Toggle Bar -->
    <div style="background: #1db954; color: white; padding: 8px 15px; border-radius: 14px 14px 0 0; font-size: 0.85rem; font-weight: bold; display: flex; justify-content: space-between; align-items: center; cursor: pointer;" onclick="toggleSpotify()">
        <span>🎵 Musik Pengiring (Hits Barat)</span>
        <span id="spotify-toggle-icon">▼</span>
    </div>
    
    <!-- Iframe Container -->
    <div id="spotify-iframe-container" style="background: #282828; border-radius: 0 0 14px 14px; padding-top: 5px; height: 152px; overflow: hidden; transition: height 0.3s ease;">
        <iframe style="border-radius: 0 0 12px 12px;" src="https://open.spotify.com/embed/playlist/37i9dQZF1DXcBWIGoYBM5M?utm_source=generator&theme=0" width="100%" height="152" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>
    </div>
</div>

<script>
    function toggleSpotify() {
        const container = document.getElementById('spotify-iframe-container');
        const icon = document.getElementById('spotify-toggle-icon');
        if (container.style.height === '0px' || container.style.height === '0') {
            container.style.height = '152px';
            icon.innerText = '▼';
        } else {
            container.style.height = '0px';
            icon.innerText = '▲';
        }
    }
    
    // Automatically minimize after 10 seconds to not block view, but user can open it
    setTimeout(() => {
        const container = document.getElementById('spotify-iframe-container');
        if(container && container.style.height !== '0px') {
            toggleSpotify();
        }
    }, 10000);
</script>
"""

# Insert before </body>
text = text.replace('</body>', spotify_widget + '\n</body>')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Spotify widget added.")
