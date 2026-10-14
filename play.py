import random
import streamlit as st
import streamlit.components.v1 as components

# ตั้งค่าหน้าเว็บหลัก
st.set_page_config(page_title="Mini Arcade Hub 🎮", page_icon="🕹️", layout="centered")

# สร้าง Sidebar สำหรับเลือกเกม
st.sidebar.title("🕹️ เลือกเกมที่คุณต้องการเล่น")
game_mode = st.sidebar.selectbox(
    "เลือกเกม:",
    ["🎲 ทอยลูกเต๋า 3D (Multi-Dice)", "💣 เกมสุ่มเลือกระเบิด (Bomb Sweeper)"]
)

st.sidebar.markdown("---")
st.sidebar.info("💡 สามารถเลือกเปลี่ยนเกมได้ตลอดเวลาในลิงก์นี้เลย!")

# ==========================================
# 1. เกมทอยลูกเต๋า 3D
# ==========================================
if game_mode == "🎲 ทอยลูกเต๋า 3D (Multi-Dice)":
    st.title("🎲 เกมทอยลูกเต๋า 3D แบบหลายลูก")
    st.write("เลือกจำนวนลูกเต๋า แล้วกดทอยเพื่อดูแอนิเมชันหมุน 3D พร้อมกัน!")

    multi_dice_html = """
    <!DOCTYPE html>
    <html>
    <head>
    <style>
      body {
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        min-height: 480px;
        margin: 0;
        background-color: transparent;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
      }
      .controls {
        display: flex;
        align-items: center;
        gap: 12px;
        margin-bottom: 30px;
        background: #f0f2f6;
        padding: 10px 20px;
        border-radius: 12px;
      }
      .controls label {
        font-weight: bold;
        color: #31333F;
        font-size: 16px;
      }
      .controls select {
        padding: 6px 12px;
        font-size: 16px;
        border-radius: 6px;
        border: 1px solid #ccc;
        outline: none;
        cursor: pointer;
      }
      .dice-container {
        display: flex;
        flex-wrap: wrap;
        justify-content: center;
        align-items: center;
        gap: 40px;
        width: 100%;
        min-height: 200px;
        margin-bottom: 25px;
        padding: 10px;
        box-sizing: border-box;
      }
      .scene {
        width: 100px;
        height: 100px;
        perspective: 600px;
      }
      .cube {
        width: 100%;
        height: 100%;
        position: relative;
        transform-style: preserve-3d;
        transform: translateZ(-50px) rotateX(0deg) rotateY(0deg);
        transition: transform 1.2s cubic-bezier(0.2, 0.8, 0.2, 1.25);
      }
      .face {
        position: absolute;
        width: 100px;
        height: 100px;
        background: #ffffff;
        border: 3px solid #222;
        border-radius: 16px;
        display: grid;
        grid-template: repeat(3, 1fr) / repeat(3, 1fr);
        padding: 8px;
        box-sizing: border-box;
        box-shadow: inset 0 0 12px rgba(0,0,0,0.15);
      }
      .dot {
        display: block;
        width: 15px;
        height: 15px;
        background-color: #333;
        border-radius: 50%;
        align-self: center;
        justify-self: center;
      }
      .dot.red { background-color: #e74c3c; }
      .front  { transform: rotateY(0deg) translateZ(50px); }
      .right  { transform: rotateY(90deg) translateZ(50px); }
      .back   { transform: rotateY(180deg) translateZ(50px); }
      .left   { transform: rotateY(-90deg) translateZ(50px); }
      .top    { transform: rotateX(90deg) translateZ(50px); }
      .bottom { transform: rotateX(-90deg) translateZ(50px); }

      .f1 .d1 { grid-area: 2/2; }
      .f2 .d1 { grid-area: 1/1; } .f2 .d2 { grid-area: 3/3; }
      .f3 .d1 { grid-area: 1/1; } .f3 .d2 { grid-area: 2/2; } .f3 .d3 { grid-area: 3/3; }
      .f4 .d1 { grid-area: 1/1; } .f4 .d2 { grid-area: 1/3; } .f4 .d3 { grid-area: 3/1; } .f4 .d4 { grid-area: 3/3; }
      .f5 .d1 { grid-area: 1/1; } .f5 .d2 { grid-area: 1/3; } .f5 .d3 { grid-area: 2/2; } .f5 .d4 { grid-area: 3/1; } .f5 .d5 { grid-area: 3/3; }
      .f6 .d1 { grid-area: 1/1; } .f6 .d2 { grid-area: 1/3; } .f6 .d3 { grid-area: 2/1; } .f6 .d4 { grid-area: 2/3; } .f6 .d5 { grid-area: 3/1; } .f6 .d6 { grid-area: 3/3; }

      .roll-btn {
        background-color: #ff4b4b;
        color: white;
        border: none;
        padding: 12px 32px;
        font-size: 18px;
        font-weight: bold;
        border-radius: 8px;
        cursor: pointer;
        box-shadow: 0 4px 12px rgba(255, 75, 75, 0.3);
        transition: all 0.2s ease;
      }
      .roll-btn:hover { background-color: #e03e3e; transform: translateY(-2px); }
      .result-box { margin-top: 20px; text-align: center; }
      .result-text { font-size: 20px; font-weight: bold; color: #1e8e3e; }
      .sub-text { font-size: 14px; color: #666; margin-top: 4px; }
    </style>
    </head>
    <body>
      <div class="controls">
        <label for="diceCount">จำนวนลูกเต๋า:</label>
        <select id="diceCount" onchange="renderDice()">
          <option value="1">1 ลูก</option>
          <option value="2" selected>2 ลูก</option>
          <option value="3">3 ลูก</option>
          <option value="4">4 ลูก</option>
          <option value="5">5 ลูก</option>
        </select>
      </div>
      <div class="dice-container" id="diceContainer"></div>
      <button class="roll-btn" onclick="rollAllDice()">🎲 ทอยลูกเต๋า!</button>
      <div class="result-box">
        <div class="result-text" id="totalResult">ผลรวม: 2 แต้ม</div>
        <div class="sub-text" id="detailResult">แต้มแต่ละลูก: [1]</div>
      </div>
    <script>
      let rollCounter = 0;
      const rotationMap = {
        1: { x: 0, y: 0 }, 2: { x: 0, y: -90 }, 3: { x: -90, y: 0 },
        4: { x: 90, y: 0 }, 5: { x: 0, y: 90 }, 6: { x: 0, y: 180 }
      };
      function createDiceHTML(id) {
        return `
          <div class="scene">
            <div class="cube" id="dice-${id}">
              <div class="face front f1"><span class="dot red d1"></span></div>
              <div class="face right f2"><span class="dot d1"></span><span class="dot d2"></span></div>
              <div class="face top f3"><span class="dot d1"></span><span class="dot d2"></span><span class="dot d3"></span></div>
              <div class="face bottom f4"><span class="dot d1"></span><span class="dot d2"></span><span class="dot d3"></span><span class="dot d4"></span></div>
              <div class="face left f5"><span class="dot d1"></span><span class="dot d2"></span><span class="dot d3"></span><span class="dot d4"></span><span class="dot d5"></span></div>
              <div class="face back f6"><span class="dot d1"></span><span class="dot d2"></span><span class="dot d3"></span><span class="dot d4"></span><span class="dot d5"></span><span class="dot d6"></span></div>
            </div>
          </div>
        `;
      }
      function renderDice() {
        const count = parseInt(document.getElementById('diceCount').value);
        const container = document.getElementById('diceContainer');
        container.innerHTML = '';
        for (let i = 0; i < count; i++) { container.innerHTML += createDiceHTML(i); }
        document.getElementById('totalResult').innerText = `ผลรวม: ${count} แต้ม`;
        document.getElementById('detailResult').innerText = `แต้มแต่ละลูก: [${Array(count).fill(1).join(', ')}]`;
      }
      function rollAllDice() {
        const count = parseInt(document.getElementById('diceCount').value);
        rollCounter += 1;
        let results = []; let totalScore = 0;
        for (let i = 0; i < count; i++) {
          const rolledVal = Math.floor(Math.random() * 6) + 1;
          results.push(rolledVal); totalScore += rolledVal;
          const dice = document.getElementById(`dice-${i}`);
          const randomExtraSpin = (Math.floor(Math.random() * 2) + 2) * 360;
          const extraTurns = rollCounter * 720 + randomExtraSpin;
          const targetX = rotationMap[rolledVal].x + extraTurns;
          const targetY = rotationMap[rolledVal].y + extraTurns;
          dice.style.transform = `translateZ(-50px) rotateX(${targetX}deg) rotateY(${targetY}deg)`;
        }
        setTimeout(() => {
          document.getElementById('totalResult').innerText = `🏆 ผลรวมทั้งหมด: ${totalScore} แต้ม`;
          document.getElementById('detailResult').innerText = `แต้มแต่ละลูก: [${results.join(', ')}]`;
        }, 1200);
      }
      renderDice();
    </script>
    </body>
    </html>
    """
    components.html(multi_dice_html, height=520)

# ==========================================
# 2. เกมสุ่มเลือกระเบิด
# ==========================================
elif game_mode == "💣 เกมสุ่มเลือกระเบิด (Bomb Sweeper)":
    st.title("💣 เกมสุ่มเลือกระเบิด (Find the Bomb)")
    st.write("มีป้าย 15 ช่อง ซ่อนระเบิดไว้ 1 ช่อง (สุ่มเปลี่ยนตำแหน่งทุกรอบ) กดโดนระเบิดเมื่อไหร่เริ่มใหม่ทันที!")

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
      .card:hover { background: #3d405b; transform: translateY(-2px); }
      .card.safe { background: #2a9d8f; color: white; cursor: default; transform: scale(0.95); }
      .card.bomb { background: #e76f51; color: white; cursor: default; animation: shake 0.4s ease-in-out; }
      @keyframes shake {
        0%, 100% { transform: translateX(0); }
        20%, 60% { transform: translateX(-6px); }
        40%, 80% { transform: translateX(6px); }
      }
      .controls { text-align: center; }
      .status-text {
        font-size: 20px; font-weight: bold; color: #31333F; margin-bottom: 15px; min-height: 28px;
      }
      .reset-btn {
        background-color: #ff4b4b; color: white; border: none; padding: 12px 28px;
        font-size: 16px; font-weight: bold; border-radius: 8px; cursor: pointer;
        box-shadow: 0 4px 10px rgba(255, 75, 75, 0.3); transition: all 0.2s ease;
      }
      .reset-btn:hover { background-color: #e03e3e; transform: translateY(-2px); }
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
        if (isGameOver || card.classList.contains('safe') || card.classList.contains('bomb')) return;

        if (index === bombIndex) {
          card.classList.add('bomb');
          card.innerText = '💥';
          isGameOver = true;
          document.getElementById('status').innerText = '💥 โดนระเบิด! กดเริ่มเกมใหม่';
          document.getElementById('status').style.color = '#e76f51';
          revealAll();
        } else {
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
