"""
Bikolpo — Safest Route Finder with Splash Screen
"""




import os
import requests
import pandas as pd
import streamlit as st
import folium
from streamlit_folium import st_folium




# ---------------- Page Config ----------------
st.set_page_config(page_title="Bikolpo — Safest Route Finder", layout="wide", page_icon="🌊")




# ---------------- Session State ----------------
if "show_splash" not in st.session_state:
    st.session_state.show_splash = True




# ---------------- Splash Screen ----------------
def show_splash_screen():
    st.markdown(
        """
        <style>
        /* Prevent code blocks */
        pre, code, .stMarkdown pre, .stMarkdown code, .stCodeBlock {
            display: none !important;
            visibility: hidden !important;
        }
       
        /* Hide Streamlit elements */
        header[data-testid="stHeader"] { display: none !important; }
        .block-container { padding: 0 !important; max-width: 100% !important; }
        .stApp { background: #ffffff !important; }
       
        /* Force button to be visible and styled */
        .element-container:has(.stButton) {
            position: fixed !important;
            bottom: 20vh !important;
            left: 50% !important;
            transform: translateX(-50%) !important;
            z-index: 10000 !important;
        }
       
        div[data-testid="column"] {
            z-index: 10000 !important;
        }
       
        .stButton > button {
            background: #105dad !important;
            color: #ffffff !important;
            border: none !important;
            border-radius: 25px !important;
            padding: 14px 40px !important;
            font-size: 16px !important;
            font-weight: 600 !important;
            cursor: pointer !important;
            transition: all 0.3s ease !important;
            min-width: 160px !important;
            animation: fadeInButton 0.8s ease-out 1.8s forwards !important;
            opacity: 0;
        }
       
        .stButton > button:hover {
            transform: translateY(-2px) !important;
            box-shadow: 0 8px 20px rgba(16, 93, 173, 0.3) !important;
            background: #0d4a8a !important;
        }
       
        /* Splash container */
        .splash-container {
            position: fixed;
            top: 0;
            left: 0;
            width: 100vw;
            height: 100vh;
            background: #ffffff;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            z-index: 9999;
        }
       
        /* Liquid animation */
        .liquid-wrapper {
            position: relative;
            width: 200px;
            height: 200px;
            margin-bottom: 40px;
        }
       
        .droplet {
            position: absolute;
            background: #105dad;
            border-radius: 50%;
            opacity: 0;
            animation: dropletAnimation 2s ease-out forwards;
        }
       
        .droplet:nth-child(1) {
            width: 120px;
            height: 120px;
            top: 60px;
            left: 40px;
            animation-delay: 0s;
        }
       
        .droplet:nth-child(2) {
            width: 150px;
            height: 150px;
            top: 50px;
            left: 30px;
            animation-delay: 0.3s;
        }
       
        .droplet:nth-child(3) {
            width: 180px;
            height: 180px;
            top: 40px;
            left: 20px;
            animation-delay: 0.6s;
        }
       
        @keyframes dropletAnimation {
            0% {
                transform: scale(0);
                opacity: 0;
            }
            50% {
                opacity: 0.8;
            }
            100% {
                transform: scale(1);
                opacity: 0;
            }
        }
       
        /* Logo */
        .splash-logo {
            font-size: 48px;
            font-weight: 700;
            color: #105dad;
            margin-bottom: 100px;
            animation: fadeIn 0.8s ease-out 1.5s forwards;
            opacity: 0;
        }
       
        @keyframes fadeIn {
            to {
                opacity: 1;
            }
        }
       
        @keyframes fadeInButton {
            to {
                opacity: 1;
            }
        }
        </style>
       
        <div class="splash-container">
            <div class="liquid-wrapper">
                <div class="droplet"></div>
                <div class="droplet"></div>
                <div class="droplet"></div>
            </div>
            <div class="splash-logo">বিকল্প</div>
        </div>
        """,
        unsafe_allow_html=True
    )
   
    # Button positioned with absolute positioning via CSS
    if st.button("Get Started", key="splash_btn"):
        st.session_state.show_splash = False
        st.rerun()




# ---------------- Main App ----------------
def main_app():
    LOGO_PATH = "logo.png"
   
    # Global Styles
    st.markdown(
        """
        <style>
          .stApp { background:#fff; color:#111827; }
          .block-container { max-width:1200px; padding-top:14px; padding-bottom:24px; }
          header[data-testid="stHeader"] { background:transparent; }
          h1, h2, h3, h4 { color:#0f172a; letter-spacing:-0.01em; }
          .muted { color:#6b7280; }
         
          div[data-testid="stNotification"] { display:none !important; }
          .stAlert { display:none !important; }
         
          .stTextInput > div > div > input {
            background:#fff; color:#111827; border:1px solid #e5e7eb;
            border-radius:12px; height:44px; padding:10px 12px;
            box-shadow:0 1px 0 rgba(0,0,0,0.02) inset;
          }
         
          label[data-testid="stWidgetLabel"] {
            color:#111827 !important;
          }
         
          .card .stTextInput {
            display:none !important;
          }
         
          .stButton > button[kind="primary"]{
            background:#2563eb; color:#fff; border-radius:12px;
            border:0; padding:10px 28px;
            min-width:200px;
            min-height:44px; line-height:1.15; font-weight:600; transition:.2s;
          }
          .stButton > button[kind="primary"]:hover { background:#1d4ed8; transform:translateY(-1px); }
          .stButton > button[kind="secondary"]{
            background:#fff; color:#111827; border-radius:12px; border:1px solid #e5e7eb;
            padding:10px 28px; min-height:44px; line-height:1.15; font-weight:600;
          }
          .stButton > button[kind="secondary"]:hover { background:#f9fafb; }
         
          .card {
            border-radius:14px; background:#fff; border:1px solid #e5e7eb;
            box-shadow:0 6px 18px rgba(17,24,39,.06);
            transition:.2s;
          }
          .card:hover { border-color:#dbeafe; box-shadow:0 10px 24px rgba(17,24,39,.08); }
          .card-inner{ padding:16px 16px; }
          .card-selected { border:2px solid #3b82f6; box-shadow:0 0 0 4px rgba(59,130,246,.12); }
         
          .stTabs [data-baseweb="tab-list"] {
            gap:8px; background:#f3f4f6; border-radius:12px; padding:6px; border:1px solid #e5e7eb;
          }
          .stTabs [data-baseweb="tab"] {
            background:transparent; border-radius:10px; color:#6b7280; font-weight:600;
            padding:8px 18px;
          }
          .stTabs [data-baseweb="tab"]:hover { background:#e5e7eb; color:#111827; }
          .stTabs [aria-selected="true"] { background:#2563eb !important; color:#fff !important; }
         
          div[data-testid="stExpander"] {
            background:transparent;
          }
          div[data-testid="stExpander"] > details {
            background:#f9fafb !important; border:1px solid #e5e7eb; border-radius:12px; padding:6px 10px;
          }
          div[data-testid="stExpander"] > details > summary {
            color:#111827 !important; font-weight:600;
            background:transparent !important;
            list-style:none;
          }
          div[data-testid="stExpander"] > details > summary > span {
            color:#111827 !important;
          }
         
          .badge { font-size:12px; font-weight:700; padding:6px 10px; border-radius:999px; display:inline-block; }
          .badge-safe { background:#ecfdf5; color:#065f46; border:1px solid #a7f3d0; }
          .badge-mod  { background:#fffbeb; color:#92400e; border:1px solid #fde68a; }
          .pill { font-size:12px; padding:6px 10px; border-radius:10px; background:#f9fafb; border:1px solid #e5e7eb; }
         
          .reason-item {
            background:#f9fafb; border:1px solid #e5e7eb; border-radius:10px;
            padding:10px 12px; margin:6px 0; display:flex; align-items:center; gap:8px;
          }
         
          .empty {
            height:540px; display:flex; align-items:center; justify-content:center;
            background:#ffffff; border:1px dashed #e5e7eb; border-radius:12px; color:#6b7280;
          }
         
          .folium-map, .st-emotion-cache-1y4p8pa { border-radius:12px; overflow:hidden; }
         
          .confetti { position:fixed; width:10px; height:10px; background:#10b981; animation:confetti-fall 3s ease-out forwards; }
          @keyframes confetti-fall { to { transform:translateY(100vh) rotate(360deg); opacity:0; } }
        </style>
       
        <script>
          function triggerConfetti() {
            const colors = ['#10b981', '#3b82f6', '#f59e0b', '#ef4444'];
            for (let i=0;i<50;i++){
              setTimeout(()=>{ const c=document.createElement('div'); c.className='confetti';
                c.style.left=Math.random()*window.innerWidth+'px';
                c.style.background=colors[Math.floor(Math.random()*colors.length)];
                c.style.animationDelay=Math.random()*0.5+'s';
                document.body.appendChild(c); setTimeout(()=>c.remove(),3000);}, i*30);
            }
          }
        </script>
        """,
        unsafe_allow_html=True
    )
   
    # Header
    col_logo, col_title = st.columns([0.06, 0.94])
    with col_logo:
        if os.path.exists(LOGO_PATH):
            st.image(LOGO_PATH, use_column_width=False, width=56)
        else:
            st.markdown("<div style='font-size:40px;line-height:1'>🌊</div>", unsafe_allow_html=True)
   
    with col_title:
        st.markdown("<h1 style='margin:0'>Bikolpo — Safest Route Finder</h1>", unsafe_allow_html=True)
        st.markdown("<div class='muted' style='margin-top:2px'>AI-powered flood-aware routing for Dhaka</div>", unsafe_allow_html=True)
   
    st.markdown("")
   
    # Tabs
    tabs = st.tabs(["🚗 Rickshaw/Car", "🚶 Walking"])
   
    # Session State
    if "routes_data" not in st.session_state:
        st.session_state.routes_data = None
    if "selected_route" not in st.session_state:
        st.session_state.selected_route = 0
    if "profile" not in st.session_state:
        st.session_state.profile = "driving-car"
    if "confetti_triggered" not in st.session_state:
        st.session_state.confetti_triggered = False
   
    # Tab: Driving
    with tabs[0]:
        st.session_state.profile = "driving-car"
       
        c1, c2, c3 = st.columns([0.40, 0.40, 0.20])
        with c1:
            source = st.text_input("📍 Starting Point", "Mirpur", key="src_car")
        with c2:
            destination = st.text_input("🎯 Destination", "Motijheel", key="dst_car")
        with c3:
            st.write("")
            fetch_car = st.button("🔎 Find Safe Routes", type="primary", use_container_width=True, key="fetch_car")
       
        if fetch_car:
            st.session_state.confetti_triggered = False
            with st.spinner("🤖 Analyzing flood zones..."):
                try:
                    resp = requests.post(
                        "http://127.0.0.1:8000/predict",
                        json={"source": source, "destination": destination, "profile": "driving-car"},
                        timeout=90,
                    )
                    if resp.status_code == 200:
                        st.session_state.routes_data = resp.json()
                        st.session_state.selected_route = 0
                        st.success("✅ Routes ready!")
                    else:
                        st.error(f"❌ {resp.text}")
                except Exception as e:
                    st.error(f"❌ {e}")
   
    # Tab: Walking
    with tabs[1]:
        st.session_state.profile = "foot-walking"
       
        c1, c2, c3 = st.columns([0.40, 0.40, 0.20])
        with c1:
            source_walk = st.text_input("📍 Starting Point", "Dhanmondi", key="src_walk")
        with c2:
            destination_walk = st.text_input("🎯 Destination", "Gulshan", key="dst_walk")
        with c3:
            st.write("")
            fetch_walk = st.button("🔎 Find Safe Routes", type="primary", use_container_width=True, key="fetch_walk")
       
        if fetch_walk:
            st.session_state.confetti_triggered = False
            with st.spinner("🤖 Analyzing walking routes..."):
                try:
                    resp = requests.post(
                        "http://127.0.0.1:8000/predict",
                        json={"source": source_walk, "destination": destination_walk, "profile": "foot-walking"},
                        timeout=90,
                    )
                    if resp.status_code == 200:
                        st.session_state.routes_data = resp.json()
                        st.session_state.selected_route = 0
                        st.success("✅ Routes ready!")
                    else:
                        st.error(f"❌ {resp.text}")
                except Exception as e:
                    st.error(f"❌ {e}")
   
    data = st.session_state.routes_data
   
    # Layout: Map + Cards
    left, right = st.columns([0.62, 0.38])
   
    # Map
    with left:
        st.markdown("<div class='card'><div class='card-inner'>", unsafe_allow_html=True)
       
        if not data:
            st.markdown("<div class='empty'>🗺️ Select locations and click 'Find Safe Routes'</div>", unsafe_allow_html=True)
        else:
            i = st.session_state.selected_route
            feature = data["routes"]["features"][i]
            info = data["route_info"][i]
           
            coords = feature["geometry"]["coordinates"]
            geom_latlon = [(lat, lon) for lon, lat in coords]
            center_lat = sum(lat for lat, _ in geom_latlon) / len(geom_latlon)
            center_lon = sum(lon for _, lon in geom_latlon) / len(geom_latlon)
            zoom = 12 if info["distance_km"] < 20 else (10 if info["distance_km"] < 100 else 8)
           
            m = folium.Map(location=[center_lat, center_lon], zoom_start=zoom, tiles="CartoDB positron")
           
            segments = info.get("segments", [])
            if segments and len(coords) >= 2:
                for idx, seg in enumerate(segments):
                    if idx + 1 >= len(coords):
                        break
                    segment_coords = [(coords[idx][1], coords[idx][0]), (coords[idx + 1][1], coords[idx + 1][0])]
                    tooltip_text = (
                        f"Segment {idx+1}<br>Flood Risk: {seg.get('risk', 0):.1%}"
                        f"<br>Length: {seg.get('length_km', 0):.2f} km"
                    )
                    folium.PolyLine(
                        segment_coords,
                        color=info.get("color", "blue"),
                        weight=6,
                        opacity=0.85,
                        tooltip=tooltip_text,
                        popup=f"<b>Flood Probability:</b> {seg.get('risk', 0):.2%}",
                    ).add_to(m)
            else:
                folium.PolyLine([(lat, lon) for lat, lon in geom_latlon], color=info.get("color", "blue"), weight=6).add_to(m)
           
            folium.Marker(
                geom_latlon[0],
                tooltip="📍 Start",
                icon=folium.Icon(color="blue", icon="play", prefix="fa"),
            ).add_to(m)
            folium.Marker(
                geom_latlon[-1],
                tooltip="🎯 Destination",
                icon=folium.Icon(color="red", icon="stop", prefix="fa"),
            ).add_to(m)
           
            st_folium(m, width=None, height=560, returned_objects=[])
       
        st.markdown("</div></div>", unsafe_allow_html=True)
   
    # Right Sidebar
    with right:
        st.markdown("<div class='card'><div class='card-inner'>", unsafe_allow_html=True)
        st.markdown("<h3 style='margin:0 0 8px 0'>Routes</h3>", unsafe_allow_html=True)
       
        if not data:
            st.markdown("<div class='muted'>No routes yet.</div>", unsafe_allow_html=True)
        else:
            df = pd.DataFrame(data["route_info"])
           
            def route_card(idx: int):
                r = df.iloc[idx]
                is_selected = st.session_state.selected_route == idx
                safe = (r.get("color", "") == "green")
                badge_cls = "badge-safe" if safe else "badge-mod"
                icon = "✅" if safe else "⚠️"
                card_class = "card card-selected" if is_selected else "card"
               
                st.markdown(
                    f"<div class='{card_class}' style='margin-bottom:14px'><div class='card-inner'>",
                    unsafe_allow_html=True,
                )
                st.markdown(f"<div class='badge {badge_cls}'>{r.get('risk_label','')}</div>", unsafe_allow_html=True)
                st.markdown(f"<h4 style='margin:8px 0 2px 0'>{icon} {r.get('route_name','Route')}</h4>", unsafe_allow_html=True)
                st.markdown(
                    f"<div class='muted'>📏 {r.get('distance_km',0)} km &nbsp;|&nbsp; ⏱️ {r.get('duration_minutes',0)} min</div>",
                    unsafe_allow_html=True,
                )
               
                rv = r.get("risk_value", 0)
                try:
                    risk_pct = float(rv)
                except Exception:
                    risk_pct = 0.0
                bar_html = f'''
                <div style="height:8px;background:#eef2f7;border-radius:6px;margin:8px 0 12px 0;overflow:hidden;">
                  <div style="height:100%;width:{risk_pct*100:.0f}%;background:{'#10b981' if safe else '#f59e0b'}"></div>
                </div>
                '''
                st.markdown(bar_html, unsafe_allow_html=True)
               
                cA, cB = st.columns([0.55, 0.45])
                with cA:
                    st.markdown(f"<span class='pill'>💧 {risk_pct:.1%} risk</span>", unsafe_allow_html=True)
                with cB:
                    if st.button(
                        "✔ Showing" if is_selected else "👁 View",
                        key=f"show_{idx}",
                        type="secondary" if is_selected else "primary",
                        use_container_width=True,
                    ):
                        st.session_state.selected_route = idx
                        if idx == 0 and not st.session_state.confetti_triggered:
                            st.session_state.confetti_triggered = True
                            st.markdown("<script>triggerConfetti();</script>", unsafe_allow_html=True)
                        st.rerun()
               
                st.markdown("</div></div>", unsafe_allow_html=True)
           
            route_card(0)
            route_card(1)
           
            if st.session_state.selected_route == 0:
                st.markdown("<div style='margin-top:20px'>", unsafe_allow_html=True)
                with st.expander("💡 Why the Safest Route?", expanded=True):
                    reasons = data.get("reasons", []) or []
                    if reasons:
                        for reason in reasons[:3]:
                            st.markdown(f"<div class='reason-item'>✓ {reason}</div>", unsafe_allow_html=True)
                    else:
                        st.markdown("<div class='muted'>Lowest flood risk path</div>", unsafe_allow_html=True)
                st.markdown("</div>", unsafe_allow_html=True)
       
        st.markdown("</div></div>", unsafe_allow_html=True)
   
    if st.session_state.selected_route == 0 and data and not st.session_state.confetti_triggered:
        st.markdown(
            """
            <script> setTimeout(function(){ triggerConfetti(); }, 500); </script>
            """,
            unsafe_allow_html=True,
        )
        st.session_state.confetti_triggered = True
   
    # Footer
    st.markdown("<hr style='border:none;border-top:1px solid #eef2f7;margin:18px 0 8px'/>", unsafe_allow_html=True)
    st.markdown(
        "<div class='muted' style='text-align:center'>"
        "<b>Bikolpo</b> · Flood-aware routing · Built with ❤️ in Dhaka</div>",
        unsafe_allow_html=True,
    )




# ---------------- Main Execution ----------------
if __name__ == "__main__":
    if st.session_state.show_splash:
        show_splash_screen()
    else:
        main_app()





