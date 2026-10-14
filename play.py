import streamlit as st
import streamlit.components.v1 as components

# ตั้งค่าหน้าเว็บ
st.set_page_config(page_title="Bomb Sweeper Game 💣", page_icon="💣", layout="centered")

st.title("💣 เกมสุ่มเลือกระเบิด ( Find the Bomb )")
st.write("มีป้าย 15 ช่อง ซ่อนระเบิดไว้ 1 ช่อง (สุ่มเปลี่ยนตำแหน่งทุกรอบ) กดโดนระเบิดเมื่อไหร่เริ่มใหม่ทันที!")

# HTML + CSS + JavaScript
bomb_game_html = """
<!DOCTYPE html>
<html>
<head>
<style>
  body {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    min-height: 500px;
    margin: 0;
    background-color: transparent;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
  }

  .grid-container {
    display: grid;
    grid-template-columns: repeat(5, 1fr);
    gap: 12px;
    width: 100%;
    max-width: 420px;
    margin-bottom: 20px;
  }

  .card {
    aspect-ratio: 1;
    background: #2b2d42;
    color: #edf2f4;
    font-size: 22px;
    font-weight: bold;
    border-radius: 12px;
    display: flex;
    justify-content: center;
    align-items: center;
    cursor: pointer;
    box-shadow: 0 4px 8px rgba(0,0,0,0.2);
    transition: all 0.2s ease;
    user-select: none;
  }

  .card:hover {
    background: #3d405b;
    transform: translateY(-2px);
  }

  .card.safe {
    background: #2a9d8f;
    color: white;
    cursor: default;
    transform: scale(0.95);
  }

  .card.bomb {
    background: #e76f51;
    color: white;
    cursor: default;
    animation: shake 0.4s ease-in-out;
  }

  @keyframes shake {
    0%, 100% { transform: translateX(0); }
    20%, 60% { transform: translateX(-6px); }
    40%, 80% { transform: translateX(6px); }
  }

  .controls {
    text-align: center;
  }

  .status-text {
    font-size: 20px;
    font-weight: bold;
    color: #31333F;
    margin-bottom: 15px;
    min-height: 28px;
  }

  .reset-btn {
    background-color: #ff4b4b;
    color: white;
    border: none;
    padding: 12px 28px;
    font-size: 16px;
    font-weight: bold;
    border-radius: 8px;
    cursor: pointer;
    box-shadow: 0 4px 10px rgba(255, 75, 75, 0.3);
    transition: all 0.2s ease;
  }

  .reset-btn:hover {
    background-color: #e03e3e;
    transform: translateY(-2px);
  }
</style>
</head>
<body>

  <div class="grid-container" id="grid"></div>

  <div class="controls">
    <div class="status-text" id="status">เปิดได้: 0 / 14 ช่อง</div>
    <button class="reset-btn" onclick="initGame()">🎮 เริ่มเกมใหม่</button>
  </div>

<script>
  const TOTAL_BOXES = 15;
  let bombIndex = -1;
  let openedCount = 0;
  let isGameOver = false;

  function initGame() {
    const grid = document.getElementById('grid');
    grid.innerHTML = '';
    
    // สุ่มตำแหน่งระเบิดใหม่
    bombIndex = Math.floor(Math.random() * TOTAL_BOXES);
    openedCount = 0;
    isGameOver = false;

    document.getElementById('status').innerText = 'เปิดได้: 0 / 14 ช่อง';
    document.getElementById('status').style.color = '#31333F';

    for (let i = 0; i < TOTAL_BOXES; i++) {
      const card = document.createElement('div');
      card.className = 'card';
      card.innerText = i + 1;
      card.onclick = () => revealCard(card, i);
      grid.appendChild(card);
    }
  }

  function revealCard(card, index) {
    if (isGameOver || card.classList.contains('safe') || card.classList.contains('bomb')) {
      return;
    }

    // โดนระเบิด
    if (index === bombIndex) {
      card.classList.add('bomb');
      card.innerText = '💥';
      isGameOver = true;
      document.getElementById('status').innerText = '💥 โดนระเบิด! กดเริ่มเกมใหม่';
      document.getElementById('status').style.color = '#e76f51';
      revealAll();
    } else {
      // เปิดได้ช่องปลอดภัย
      card.classList.add('safe');
      card.innerText = '🪙';
      openedCount++;

      if (openedCount === TOTAL_BOXES - 1) {
        isGameOver = true;
        document.getElementById('status').innerText = '🎉 ชนะแล้ว! เปิดครบทุกช่องปลอดภัย';
        document.getElementById('status').style.color = '#2a9d8f';
        revealAll();
      } else {
        document.getElementById('status').innerText = `เปิดได้: ${openedCount} / 14 ช่อง`;
      }
    }
  }

  function revealAll() {
    const cards = document.querySelectorAll('.card');
    cards.forEach((card, idx) => {
      if (idx === bombIndex) {
        card.classList.add('bomb');
        card.innerText = '💥';
      }
    });
  }

  initGame();
</script>

</body>
</html>
"""

components.html(bomb_game_html, height=520)
#streamlit run play.py