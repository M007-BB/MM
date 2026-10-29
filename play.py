import random
import streamlit as st
import streamlit.components.v1 as components

# Page Configuration
st.set_page_config(
    page_title="Mini Arcade & Party Hub 🎮",
    page_icon="🍻",
    layout="centered",
    initial_sidebar_state="expanded"
)

# Custom Styling for Streamlit Shell
st.markdown("""
<style>
    .stApp {
        background-color: #0d1117;
        color: #f0f6fc;
    }
    .css-1d38152, [data-testid="stSidebar"] {
        background-color: #161b22 !important;
    }
    h1, h2, h3 {
        color: #58a6ff !important;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    }
</style>
""", unsafe_allow_html=True)

# Sidebar Navigation
st.sidebar.title("🕹️ Mini Arcade Hub")
game_mode = st.sidebar.selectbox(
    "เลือกเกมที่คุณต้องการเล่น:",
    [
        "🍾 เกมหมุนขวดเบียร์ดิจิทัล 3D (Beer Spin the Bottle)",
        "🎲 ทอยลูกเต๋า 3D (Multi-Dice Roller)", 
        "💣 เกมสุ่มเลือกระเบิด (Bomb Sweeper)"
    ]
)

st.sidebar.markdown("---")
st.sidebar.info("💡 สลับเปลี่ยนเกมได้ตลอดเวลา ทั้งหมดรวมอยู่ในลิงก์เดียว!")

# ==========================================
# 1. SLEEK 3D BEER BOTTLE SPIN GAME
# ==========================================
if game_mode == "🍾 เกมหมุนขวดเบียร์ดิจิทัล 3D (Beer Spin the Bottle)":
    st.title("🍾 เกมหมุนขวดเบียร์ดิจิทัล (Beer Spin)")
    st.write("วางมือถือไว้กลางวง เลือกจำนวนเพื่อนในวงเหล้า แล้วกดหมุนขวดเบียร์แก้วอำพันเสี่ยงทายได้เลย!")

    spin_bottle_html = """
    <!DOCTYPE html>
    <html lang="th">
    <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
      * {
        box-sizing: border-box;
        user-select: none;
      }
      body {
        margin: 0;
        padding: 10px;
        background: #0b0f19;
        color: #f3f4f6;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        min-height: 560px;
        overflow: hidden;
      }

      .control-panel {
        display: flex;
        flex-wrap: wrap;
        gap: 12px;
        justify-content: center;
        align-items: center;
        background: rgba(31, 41, 55, 0.7);
        backdrop-filter: blur(10px);
        padding: 10px 18px;
        border-radius: 16px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        margin-bottom: 15px;
        width: 100%;
        max-width: 480px;
      }

      .control-group {
        display: flex;
        align-items: center;
        gap: 8px;
      }
      .control-group label {
        font-size: 13px;
        font-weight: 600;
        color: #9ca3af;
      }
      .control-group select {
        background: #111827;
        color: #f59e0b;
        border: 1px solid #374151;
        padding: 6px 12px;
        border-radius: 8px;
        font-size: 13px;
        font-weight: bold;
        outline: none;
        cursor: pointer;
      }

      /* Circular Lounge Table */
      .table-area {
        position: relative;
        width: 320px;
        height: 320px;
        display: flex;
        justify-content: center;
        align-items: center;
        margin-bottom: 20px;
      }

      .table-outer-ring {
        position: absolute;
        width: 300px;
        height: 300px;
        border-radius: 50%;
        background: radial-gradient(circle, #1e293b 0%, #0f172a 70%, #020617 100%);
        border: 3px solid rgba(245, 158, 11, 0.3);
        box-shadow: 0 0 35px rgba(245, 158, 11, 0.15), inset 0 0 20px rgba(0,0,0,0.8);
      }

      .table-inner-glow {
        position: absolute;
        width: 220px;
        height: 220px;
        border-radius: 50%;
        border: 1.5px dashed rgba(245, 158, 11, 0.4);
        animation: pulseGlow 4s infinite alternate ease-in-out;
      }
      @keyframes pulseGlow {
        0% { box-shadow: 0 0 10px rgba(245, 158, 11, 0.2); }
        100% { box-shadow: 0 0 25px rgba(245, 158, 11, 0.5); }
      }

      /* Player Seats Around Table */
      .player-seat {
        position: absolute;
        width: 36px;
        height: 36px;
        border-radius: 50%;
        background: #1f2937;
        border: 2px solid #f59e0b;
        color: #f3f4f6;
        font-size: 13px;
        font-weight: bold;
        display: flex;
        justify-content: center;
        align-items: center;
        box-shadow: 0 0 10px rgba(245, 158, 11, 0.4);
        transition: all 0.3s ease;
        z-index: 5;
      }
      .player-seat.selected {
        background: #ef4444;
        border-color: #fff;
        color: #fff;
        transform: scale(1.35) !important;
        box-shadow: 0 0 25px #ef4444, 0 0 45px #ef4444;
        z-index: 10;
      }

      /* 3D Realistic Amber Beer Bottle */
      .bottle-wrapper {
        position: relative;
        width: 70px;
        height: 240px;
        display: flex;
        justify-content: center;
        align-items: center;
        transform-origin: 50% 50%;
        transition: transform 3.8s cubic-bezier(0.1, 0.85, 0.1, 1);
        filter: drop-shadow(0 15px 15px rgba(0, 0, 0, 0.85));
        z-index: 6;
      }

      .beer-bottle {
        position: relative;
        width: 54px;
        height: 220px;
        display: flex;
        flex-direction: column;
        align-items: center;
      }

      /* Gold Crown Cap (ฝาจีบขวดเบียร์) */
      .beer-cap {
        width: 18px;
        height: 12px;
        background: linear-gradient(90deg, #b45309, #fde047, #f59e0b, #78350f);
        border-radius: 3px 3px 1px 1px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.6);
        z-index: 4;
        border-bottom: 2px solid #78350f;
      }

      /* Neck Ring */
      .beer-neck-ring {
        width: 20px;
        height: 6px;
        background: linear-gradient(90deg, #78350f, #d97706, #451a03);
        margin-top: -1px;
        z-index: 3;
      }

      /* Long Neck (คอขวดเบียร์) */
      .beer-neck {
        width: 22px;
        height: 75px;
        background: linear-gradient(
          90deg,
          rgba(251, 191, 36, 0.4) 0%,
          rgba(180, 83, 9, 0.95) 25%,
          rgba(120, 53, 15, 1) 70%,
          rgba(69, 26, 3, 0.9) 100%
        );
        border-radius: 4px 4px 0 0;
        box-shadow: inset 2px 0 4px rgba(255, 255, 255, 0.4);
        position: relative;
      }

      /* Neck Foil/Label (ฉลากคอขวด) */
      .beer-neck-label {
        position: absolute;
        top: 25px;
        width: 100%;
        height: 20px;
        background: linear-gradient(135deg, #1e3a8a, #3b82f6, #1e3a8a);
        border-top: 1px solid #f59e0b;
        border-bottom: 1px solid #f59e0b;
        display: flex;
        justify-content: center;
        align-items: center;
        font-size: 8px;
        color: #fde047;
        font-weight: bold;
      }

      /* Shoulder Curve (ไหล่ขวด) */
      .beer-shoulder {
        width: 54px;
        height: 35px;
        background: radial-gradient(circle at 50% 0%, rgba(217, 119, 6, 0.9), rgba(120, 53, 15, 1) 80%);
        clip-path: polygon(29.6% 0%, 70.4% 0%, 100% 100%, 0% 100%);
      }

      /* Main Body (ตัวขวดเบียร์อำพัน) */
      .beer-body {
        position: relative;
        width: 54px;
        height: 100px;
        background: linear-gradient(
          90deg,
          rgba(251, 191, 36, 0.5) 0%,
          rgba(180, 83, 9, 0.95) 20%,
          rgba(120, 53, 15, 1) 60%,
          rgba(69, 26, 3, 0.95) 100%
        );
        border-radius: 0 0 16px 16px;
        box-shadow: inset 4px 0 6px rgba(255, 255, 255, 0.3), inset -4px 0 8px rgba(0, 0, 0, 0.7);
        display: flex;
        justify-content: center;
        align-items: center;
        overflow: hidden;
      }

      /* Main Beer Label (ฉลากเบียร์หลัก) */
      .beer-main-label {
        width: 44px;
        height: 52px;
        background: linear-gradient(180deg, #fef3c7 0%, #fde047 30%, #d97706 100%);
        border: 2px solid #78350f;
        border-radius: 6px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        box-shadow: 0 2px 6px rgba(0,0,0,0.5);
      }
      .label-star {
        font-size: 10px;
        color: #b91c1c;
      }
      .label-text {
        font-size: 9px;
        font-weight: 900;
        color: #451a03;
        letter-spacing: 0.5px;
        font-family: serif;
      }
      .label-sub {
        font-size: 6px;
        font-weight: bold;
        color: #78350f;
      }

      /* Glass Highlight Reflection */
      .glass-shine {
        position: absolute;
        top: 0;
        left: 6px;
        width: 5px;
        height: 100%;
        background: linear-gradient(180deg, rgba(255,255,255,0.7), rgba(255,255,255,0.1));
        border-radius: 4px;
        filter: blur(0.8px);
        pointer-events: none;
      }

      /* Result Display Card */
      .result-card {
        background: rgba(17, 24, 39, 0.85);
        backdrop-filter: blur(12px);
        border: 1px solid rgba(245, 158, 11, 0.3);
        width: 100%;
        max-width: 460px;
        padding: 16px 20px;
        border-radius: 16px;
        text-align: center;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5);
        margin-bottom: 15px;
        min-height: 90px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
      }
      .result-header {
        font-size: 13px;
        font-weight: 700;
        color: #f59e0b;
        letter-spacing: 1px;
        text-transform: uppercase;
        margin-bottom: 4px;
      }
      .result-body {
        font-size: 17px;
        font-weight: 700;
        color: #f9fafb;
        line-height: 1.4;
      }

      /* Control Button */
      .spin-btn {
        background: linear-gradient(135deg, #f59e0b 0%, #d97706 100%);
        color: #0f172a;
        border: none;
        padding: 12px 36px;
        font-size: 17px;
        font-weight: 800;
        border-radius: 12px;
        cursor: pointer;
        box-shadow: 0 4px 20px rgba(245, 158, 11, 0.4);
        transition: all 0.2s ease;
        display: flex;
        align-items: center;
        gap: 8px;
      }
      .spin-btn:hover {
        transform: translateY(-2px) scale(1.02);
        box-shadow: 0 6px 25px rgba(245, 158, 11, 0.6);
      }
      .spin-btn:disabled {
        background: #374151;
        color: #9ca3af;
        cursor: not-allowed;
        transform: none;
        box-shadow: none;
      }

      /* Confetti Canvas overlay */
      #canvas-confetti {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        pointer-events: none;
        z-index: 20;
      }
    </style>
    </head>
    <body>
      <canvas id="canvas-confetti"></canvas>

      <!-- Settings Panel -->
      <div class="control-panel">
        <div class="control-group">
          <label for="playerCount">👥 จำนวนคนในวง:</label>
          <select id="playerCount" onchange="updatePlayers()">
            <option value="2">2 คน</option>
            <option value="3">3 คน</option>
            <option value="4">4 คน</option>
            <option value="5">5 คน</option>
            <option value="6" selected>6 คน</option>
            <option value="7">7 คน</option>
            <option value="8">8 คน</option>
            <option value="9">9 คน</option>
            <option value="10">10 คน</option>
            <option value="12">12 คน</option>
          </select>
        </div>
        <div class="control-group">
          <label for="gameMode">🎯 โหมดเกม:</label>
          <select id="gameMode">
            <option value="drinking">🍻 ภารกิจวงเหล้า</option>
            <option value="truth_dare">🔥 ความจริงหรือการกระทำ</option>
            <option value="most_likely">🤫 ทายใจใครเอ่ย (Most Likely)</option>
          </select>
        </div>
      </div>

      <!-- Circular Table Display -->
      <div class="table-area" id="tableArea">
        <div class="table-outer-ring"></div>
        <div class="table-inner-glow"></div>
        <div id="seatsContainer"></div>

        <!-- 3D Realistic Beer Bottle Component -->
        <div class="bottle-wrapper" id="bottleWrapper">
          <div class="beer-bottle">
            <div class="beer-cap"></div>
            <div class="beer-neck-ring"></div>
            <div class="beer-neck">
              <div class="beer-neck-label">BEER</div>
              <div class="glass-shine"></div>
            </div>
            <div class="beer-shoulder"></div>
            <div class="beer-body">
              <div class="beer-main-label">
                <span class="label-star">★ ★ ★</span>
                <span class="label-text">LAGER</span>
                <span class="label-sub">PREMIUM</span>
              </div>
              <div class="glass-shine"></div>
            </div>
          </div>
        </div>
      </div>

      <!-- Result Card Display -->
      <div class="result-card">
        <div class="result-header" id="resultHeader">✨ พร้อมเสี่ยงดวง</div>
        <div class="result-body" id="resultBody">กดปุ่มหมุนขวดด้านล่างเพื่อชี้เลือกผู้โชคร้ายประจำรอบ!</div>
      </div>

      <button class="spin-btn" id="spinBtn" onclick="spinBottle()">🍾 หมุนขวดเลย!</button>

    <script>
      let currentAngle = 0;
      let isSpinning = false;

      const tasks = {
        drinking: [
          "🍻 ดื่ม 1 แก้วเต็มๆ แบบไม่ต้องสืบ!",
          "👉 เลือกเพื่อนซ้ายมือของคุณ 1 คนให้ดื่มแทน!",
          "👑 ได้เป็นราชา 1 รอบ! สั่งใครดื่มก็ได้ตามใจชอบ 1 คน",
          "🤫 ห้ามพูดคำว่า 'กู/มึง' เป็นเวลา 2 รอบ ใครหลุดดื่ม!",
          "🎤 เลือกเพื่อนขวามือของคุณ 1 คนให้ดื่มแทน!",
          "📸 ถ่ายรูปเซลฟี่หน้าตลกๆ ลงสตอรี่ไอจีตอนนี้!",
          "🤝 ชนแก้วกับคนที่นั่งตรงข้ามคุณและดื่ม",
          "🔄 หน้าขาววว",
          "🔄 หายจากเกม 2 รอบ",
          "🔄 เลือกเพื่อน 1 เป็นตัวแทนในรอบนี้(1รอบ)",
          "👉 หาเพื่อนดื่มด้วย2คน!",
          "👉 ดื่มแล้วย้อนศร(เปลี่ยนทางวน)",
          "👉 หาเพื่อนดื่มด้วย1คน!",
          "หมดวง🥳🥳(โดนทุกคน)",
          "15ยก (นับสูงสุด3)🥳",
          "เหมา2แก้ว ",
          "1-5โดน🥳(เลือกเลขในใจแล้วชูนิ้วขึ้นพร้อมกัน)",
          "🤫 ห้ามพูดเป็นเวลา 2 รอบ ใครหลุดดื่ม!",
          "👉 หาเพื่อนดื่มด้วย1คน!",
          "🤫 ห้ามพูดคำว่า 'กู/มึง' เป็นเวลา 2 รอบ ใครหลุดดื่ม!"
        ],   
      };

      function updatePlayers() {
        const count = parseInt(document.getElementById('playerCount').value);
        const container = document.getElementById('seatsContainer');
        container.innerHTML = '';
        const radius = 135;

        for (let i = 0; i < count; i++) {
          const angleDeg = (i * (360 / count)) - 90; // 0 deg points to top seat
          const angleRad = angleDeg * (Math.PI / 180);
          const x = Math.cos(angleRad) * radius;
          const y = Math.sin(angleRad) * radius;

          const seat = document.createElement('div');
          seat.className = 'player-seat';
          seat.id = `seat-${i}`;
          seat.innerText = `P${i + 1}`;
          seat.style.transform = `translate(${x}px, ${y}px)`;
          container.appendChild(seat);
        }
      }

      function spinBottle() {
        if (isSpinning) return;
        isSpinning = true;

        const spinBtn = document.getElementById('spinBtn');
        spinBtn.disabled = true;
        document.getElementById('resultHeader').innerText = "🍾 กำลังหมุน...";
        document.getElementById('resultBody').innerText = "ขวดเบียร์กำลังหมุนติ้วๆ ลุ้นกันว่าปากขวดจะไปหยุดที่ใคร...";

        document.querySelectorAll('.player-seat').forEach(s => s.classList.remove('selected'));

        const count = parseInt(document.getElementById('playerCount').value);
        const selectedIndex = Math.floor(Math.random() * count);
        
        const targetSeatAngle = selectedIndex * (360 / count);
        const extraTurns = (Math.floor(Math.random() * 4) + 5) * 360;
        
        currentAngle += extraTurns + targetSeatAngle - (currentAngle % 360);
        
        const wrapper = document.getElementById('bottleWrapper');
        wrapper.style.transform = `rotate(${currentAngle}deg)`;

        setTimeout(() => {
          isSpinning = false;
          spinBtn.disabled = false;

          const winnerSeat = document.getElementById(`seat-${selectedIndex}`);
          if (winnerSeat) winnerSeat.classList.add('selected');

          const mode = document.getElementById('gameMode').value;
          const missionList = tasks[mode];
          const chosenMission = missionList[Math.floor(Math.random() * missionList.length)];

          document.getElementById('resultHeader').innerText = `🎯 ผู้โชคร้าย: ผู้เล่น P${selectedIndex + 1}`;
          document.getElementById('resultBody').innerText = chosenMission;

          launchConfetti();

        }, 3800);
      }

      const confettiCanvas = document.getElementById('canvas-confetti');
      const ctx = confettiCanvas.getContext('2d');
      let particles = [];

      function resizeConfetti() {
        confettiCanvas.width = confettiCanvas.parentElement.clientWidth;
        confettiCanvas.height = confettiCanvas.parentElement.clientHeight;
      }
      window.addEventListener('resize', resizeConfetti);
      resizeConfetti();

      function launchConfetti() {
        particles = [];
        const colors = ['#f59e0b', '#38bdf8', '#fbbf24', '#ef4444', '#a855f7'];
        for (let i = 0; i < 40; i++) {
          particles.push({
            x: confettiCanvas.width / 2,
            y: confettiCanvas.height / 2,
            vx: (Math.random() - 0.5) * 10,
            vy: (Math.random() - 0.8) * 10,
            size: Math.random() * 6 + 4,
            color: colors[Math.floor(Math.random() * colors.length)],
            life: 1
          });
        }
        animateConfetti();
      }

      function animateConfetti() {
        ctx.clearRect(0, 0, confettiCanvas.width, confettiCanvas.height);
        let active = false;

        particles.forEach(p => {
          if (p.life > 0) {
            active = true;
            p.x += p.vx;
            p.y += p.vy;
            p.vy += 0.25;
            p.life -= 0.02;

            ctx.fillStyle = p.color;
            ctx.globalAlpha = Math.max(0, p.life);
            ctx.beginPath();
            ctx.arc(p.x, p.y, p.size, 0, Math.PI * 2);
            ctx.fill();
          }
        });

        if (active) requestAnimationFrame(animateConfetti);
      }

      updatePlayers();
    </script>
    </body>
    </html>
    """
    components.html(spin_bottle_html, height=630)

# ==========================================
# 2. MULTI-DICE 3D ROLLER
# ==========================================
elif game_mode == "🎲 ทอยลูกเต๋า 3D (Multi-Dice Roller)":
    st.title("🎲 เกมทอยลูกเต๋า 3D แบบหลายลูก")
    st.write("เลือกจำนวนลูกเต๋า แล้วกดทอยเพื่อดูแอนิเมชันหมุน 3D พร้อมกัน!")

    multi_dice_html = """
    <!DOCTYPE html>
    <html>
    <head>
    <style>
      body {
        display: flex; flex-direction: column; justify-content: center; align-items: center;
        min-height: 480px; margin: 0; background-color: transparent; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
      }
      .controls {
        display: flex; align-items: center; gap: 12px; margin-bottom: 30px;
        background: #1f2937; padding: 10px 20px; border-radius: 12px; border: 1px solid #374151;
      }
      .controls label { font-weight: bold; color: #f3f4f6; font-size: 16px; }
      .controls select { padding: 6px 12px; font-size: 16px; border-radius: 6px; border: 1px solid #4b5563; background: #111827; color: #fff; outline: none; cursor: pointer; }
      .dice-container {
        display: flex; flex-wrap: wrap; justify-content: center; align-items: center;
        gap: 40px; width: 100%; min-height: 200px; margin-bottom: 25px; padding: 10px; box-sizing: border-box;
      }
      .scene { width: 100px; height: 100px; perspective: 600px; }
      .cube {
        width: 100%; height: 100%; position: relative; transform-style: preserve-3d;
        transform: translateZ(-50px) rotateX(0deg) rotateY(0deg);
        transition: transform 1.2s cubic-bezier(0.2, 0.8, 0.2, 1.25);
      }
      .face {
        position: absolute; width: 100px; height: 100px; background: #ffffff;
        border: 3px solid #222; border-radius: 16px; display: grid;
        grid-template: repeat(3, 1fr) / repeat(3, 1fr); padding: 8px; box-sizing: border-box;
        box-shadow: inset 0 0 12px rgba(0,0,0,0.15);
      }
      .dot { display: block; width: 15px; height: 15px; background-color: #333; border-radius: 50%; align-self: center; justify-self: center; }
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
        background-color: #38bdf8; color: #0f172a; border: none; padding: 12px 32px;
        font-size: 18px; font-weight: bold; border-radius: 8px; cursor: pointer;
        box-shadow: 0 4px 12px rgba(56, 189, 248, 0.4); transition: all 0.2s ease;
      }
      .roll-btn:hover { background-color: #0284c7; color: white; transform: translateY(-2px); }
      .result-box { margin-top: 20px; text-align: center; }
      .result-text { font-size: 20px; font-weight: bold; color: #34d399; }
      .sub-text { font-size: 14px; color: #9ca3af; margin-top: 4px; }
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
# 3. BOMB SWEEPER GAME
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
        display: flex; flex-direction: column; justify-content: center; align-items: center;
        min-height: 500px; margin: 0; background-color: transparent; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
      }
      .grid-container {
        display: grid; grid-template-columns: repeat(5, 1fr); gap: 12px; width: 100%; max-width: 420px; margin-bottom: 20px;
      }
      .card {
        aspect-ratio: 1; background: #1f2937; color: #edf2f4; font-size: 22px; font-weight: bold;
        border-radius: 12px; display: flex; justify-content: center; align-items: center; cursor: pointer;
        box-shadow: 0 4px 8px rgba(0,0,0,0.4); border: 1px solid #374151; transition: all 0.2s ease; user-select: none;
      }
      .card:hover { background: #374151; transform: translateY(-2px); }
      .card.safe { background: #059669; color: white; cursor: default; transform: scale(0.95); }
      .card.bomb { background: #dc2626; color: white; cursor: default; animation: shake 0.4s ease-in-out; }
      @keyframes shake {
        0%, 100% { transform: translateX(0); }
        20%, 60% { transform: translateX(-6px); }
        40%, 80% { transform: translateX(6px); }
      }
      .controls { text-align: center; }
      .status-text { font-size: 20px; font-weight: bold; color: #f9fafb; margin-bottom: 15px; min-height: 28px; }
      .reset-btn {
        background-color: #ef4444; color: white; border: none; padding: 12px 28px;
        font-size: 16px; font-weight: bold; border-radius: 8px; cursor: pointer;
        box-shadow: 0 4px 10px rgba(239, 68, 68, 0.4); transition: all 0.2s ease;
      }
      .reset-btn:hover { background-color: #dc2626; transform: translateY(-2px); }
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
        document.getElementById('status').style.color = '#f9fafb';

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
          document.getElementById('status').style.color = '#ef4444';
          revealAll();
        } else {
          card.classList.add('safe');
          card.innerText = '🪙';
          openedCount++;
          if (openedCount === TOTAL_BOXES - 1) {
            isGameOver = true;
            document.getElementById('status').innerText = '🎉 ชนะแล้ว! เปิดครบทุกช่องปลอดภัย';
            document.getElementById('status').style.color = '#059669';
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
