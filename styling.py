
import streamlit as st


def apply_styles():
    st.markdown(
        """
        <style>
        /* =========================================
           MODELLAB — DESIGN SYSTEM
           Dark charcoal / rose / violet
        ========================================= */

        :root {
            --bg: #0c0a10;
            --surface: #15121c;
            --surface-hover: #1d1726;
            --surface-raised: #211a2b;
            --border: #33263d;
            --border-hover: #714264;
            --pink: #f080b7;
            --pink-bright: #ff9bce;
            --purple: #ac8aff;
            --text: #f6eef8;
            --muted: #ab9eb5;
            --green: #85e0bd;
            --radius: 18px;
        }

        /* =========================================
           GLOBAL LAYOUT
        ========================================= */

        html {
            scroll-behavior: smooth;
        }

        .stApp {
            color: var(--text);
            background:
                radial-gradient(
                    ellipse at 10% 0%,
                    rgba(218, 91, 166, 0.13),
                    transparent 32%
                ),
                radial-gradient(
                    ellipse at 95% 10%,
                    rgba(139, 92, 246, 0.13),
                    transparent 30%
                ),
                linear-gradient(
                    155deg,
                    #100d16 0%,
                    #0c0a10 48%,
                    #100d17 100%
                );
        }

        [data-testid="stHeader"] {
            background: rgba(12, 10, 16, 0.65);
        }

        [data-testid="stMain"] {
            background: transparent;
        }

        .block-container {
            max-width: 1240px;
            padding: 2.5rem 2.5rem 4rem;
        }

        /* Text hierarchy */

        html,
        body,
        [class*="css"] {
            font-family:
                Inter,
                -apple-system,
                BlinkMacSystemFont,
                "Segoe UI",
                sans-serif;
        }

        h1, h2, h3, h4 {
            color: var(--text) !important;
            font-weight: 700 !important;
            letter-spacing: -0.045em;
        }

        h1 {
            font-size: clamp(2rem, 4vw, 3.2rem) !important;
            line-height: 1.12 !important;
        }

        h2 {
            font-size: 1.55rem !important;
            margin-top: 1.5rem !important;
        }

        h3 {
            font-size: 1.13rem !important;
            letter-spacing: -0.02em;
        }

        p, li {
            color: #d0c5d6;
            line-height: 1.7;
        }

        strong {
            color: #fff3fb;
        }

        a {
            color: var(--pink-bright) !important;
            text-decoration: none !important;
        }

        a:hover {
            color: var(--purple) !important;
        }

        /* =========================================
           HERO HEADER
        ========================================= */

        .hero-card {
            position: relative;
            overflow: hidden;
            background:
                radial-gradient(
                    ellipse at 100% 0%,
                    rgba(172, 138, 255, 0.16),
                    transparent 46%
                ),
                linear-gradient(
                    125deg,
                    rgba(240, 128, 183, 0.12),
                    rgba(28, 21, 38, 0.92) 65%
                );
            border: 1px solid #483147;
            border-radius: 24px;
            padding: 36px 38px;
            margin: 0 0 28px;
            box-shadow:
                0 16px 60px rgba(0, 0, 0, 0.18),
                inset 0 1px 0 rgba(255, 255, 255, 0.035);
        }

        .hero-card::after {
            content: "";
            position: absolute;
            top: -100px;
            right: -90px;
            width: 260px;
            height: 260px;
            border-radius: 50%;
            border: 1px solid rgba(240, 128, 183, 0.12);
            box-shadow:
                0 0 0 22px rgba(240, 128, 183, 0.025),
                0 0 0 44px rgba(172, 138, 255, 0.025);
            pointer-events: none;
        }

        .hero-tag {
            display: inline-block;
            color: var(--pink-bright);
            background: rgba(240, 128, 183, 0.09);
            border: 1px solid rgba(240, 128, 183, 0.22);
            padding: 6px 11px;
            border-radius: 999px;
            font-size: 0.72rem;
            font-weight: 750;
            letter-spacing: 0.13em;
            text-transform: uppercase;
            margin-bottom: 13px;
        }

        .hero-card h1 {
            margin: 0 0 12px !important;
            font-size: clamp(2.4rem, 5vw, 3.7rem) !important;
            background: linear-gradient(
                100deg,
                #fff4fb 0%,
                #f6a8d1 48%,
                #c4aaff 100%
            );
            -webkit-background-clip: text;
            background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        .hero-description {
            max-width: 700px;
            color: #c7b8d0 !important;
            font-size: 1rem;
            line-height: 1.8;
            margin: 0;
        }

        /* =========================================
           SIDEBAR
        ========================================= */

        [data-testid="stSidebar"] {
            background: linear-gradient(
                180deg,
                #15111c 0%,
                #100d15 100%
            );
            border-right: 1px solid #302337;
        }

        [data-testid="stSidebar"] > div:first-child {
            background: transparent;
        }

        [data-testid="stSidebar"] .block-container {
            padding: 1.7rem 1.2rem 2rem;
        }

        [data-testid="stSidebar"] h1,
        [data-testid="stSidebar"] h2,
        [data-testid="stSidebar"] h3 {
            font-size: 1.15rem !important;
            letter-spacing: -0.025em;
        }

        [data-testid="stSidebar"] label,
        [data-testid="stSidebar"] label p {
            color: #d7c7df !important;
            font-size: 0.88rem !important;
            font-weight: 550;
        }

        [data-testid="stSidebar"] hr {
            border-color: #38283e;
            margin: 1.3rem 0;
        }

        /* =========================================
           METRIC CARDS
        ========================================= */

        [data-testid="stMetric"] {
            position: relative;
            background: linear-gradient(
                145deg,
                rgba(35, 26, 44, 0.95),
                rgba(20, 16, 27, 0.96)
            );
            border: 1px solid var(--border);
            border-radius: var(--radius);
            padding: 21px 22px;
            min-height: 120px;
            box-shadow: 0 8px 25px rgba(0, 0, 0, 0.12);
            transition:
                transform 180ms ease,
                border-color 180ms ease,
                box-shadow 180ms ease;
        }

        [data-testid="stMetric"]:hover {
            transform: translateY(-3px);
            border-color: var(--border-hover);
            box-shadow:
                0 12px 30px rgba(0, 0, 0, 0.22),
                0 0 22px rgba(240, 128, 183, 0.055);
        }

        [data-testid="stMetricLabel"] {
            color: var(--muted) !important;
            font-size: 0.84rem !important;
            font-weight: 600 !important;
        }

        [data-testid="stMetricValue"] {
            color: var(--pink-bright) !important;
            font-size: clamp(1.45rem, 2vw, 2rem) !important;
            font-weight: 750 !important;
            letter-spacing: -0.04em;
        }

        [data-testid="stMetricDelta"] {
            font-size: 0.82rem !important;
        }

        /* =========================================
           BUTTONS
        ========================================= */

        .stButton > button,
        .stDownloadButton > button {
            border: 1px solid #69405f;
            border-radius: 12px;
            background: linear-gradient(
                115deg,
                #d968a3,
                #a875ce
            );
            color: #fffaff !important;
            font-weight: 700;
            padding: 0.62rem 1.15rem;
            min-height: 42px;
            box-shadow: 0 5px 18px rgba(184, 92, 161, 0.12);
            transition:
                transform 160ms ease,
                filter 160ms ease,
                box-shadow 160ms ease;
        }

        .stButton > button:hover,
        .stDownloadButton > button:hover {
            transform: translateY(-2px);
            filter: brightness(1.1);
            box-shadow: 0 8px 25px rgba(184, 92, 161, 0.22);
        }

        .stButton > button:active,
        .stDownloadButton > button:active {
            transform: translateY(0);
        }

        .stButton > button:focus,
        .stDownloadButton > button:focus {
            border-color: var(--pink-bright);
            box-shadow: 0 0 0 3px rgba(240, 128, 183, 0.18);
        }

        /* =========================================
           SELECTBOXES AND INPUTS
        ========================================= */

        [data-baseweb="select"] > div {
            background: #191420 !important;
            border-color: #44334d !important;
            border-radius: 11px !important;
            transition: border-color 180ms ease;
        }

        [data-baseweb="select"] > div:hover {
            border-color: #a45d8d !important;
        }

        [data-baseweb="popover"] {
            background: #211a2b !important;
            border: 1px solid #48334f !important;
            border-radius: 12px !important;
        }

        [role="option"] {
            background: #211a2b !important;
            color: var(--text) !important;
        }

        [role="option"]:hover {
            background: #3a2540 !important;
        }

        input, textarea {
            color: var(--text) !important;
            background: #191420 !important;
            border-color: #44334d !important;
            border-radius: 10px !important;
        }

        input:focus, textarea:focus {
            border-color: var(--pink) !important;
            box-shadow: 0 0 0 2px rgba(240, 128, 183, 0.12) !important;
        }

        /* =========================================
           SLIDERS
        ========================================= */

        [data-testid="stSlider"] [data-baseweb="slider"] {
            padding-top: 0.4rem;
        }

        [data-testid="stSlider"] [role="slider"] {
            background: #fff0fa !important;
            border: 2px solid var(--pink) !important;
            box-shadow: 0 0 12px rgba(240, 128, 183, 0.28);
        }

        [data-testid="stSlider"] [data-testid="stTickBar"] {
            background: #624056;
        }

        /* =========================================
           TABS
        ========================================= */

        [data-testid="stTabs"] [role="tablist"] {
            gap: 8px;
            border-bottom: 1px solid #34263d;
        }

        [data-testid="stTabs"] button[role="tab"] {
            color: #aa9ab4;
            border-radius: 10px 10px 0 0;
            padding: 10px 16px;
            font-weight: 650;
            transition:
                color 160ms ease,
                background 160ms ease;
        }

        [data-testid="stTabs"] button[role="tab"]:hover {
            color: #f5c0df;
            background: rgba(240, 128, 183, 0.055);
        }

        [data-testid="stTabs"] button[role="tab"][aria-selected="true"] {
            color: var(--pink-bright) !important;
            background: rgba(240, 128, 183, 0.075);
        }

        [data-testid="stTabs"] [data-baseweb="tab-highlight"] {
            background: linear-gradient(
                90deg,
                var(--pink),
                var(--purple)
            ) !important;
            height: 3px;
            border-radius: 5px;
        }

        /* =========================================
           EXPANDERS
        ========================================= */

        [data-testid="stExpander"] {
            background: rgba(24, 19, 32, 0.83);
            border: 1px solid #37283f;
            border-radius: 15px;
            overflow: hidden;
            transition: border-color 180ms ease;
        }

        [data-testid="stExpander"]:hover {
            border-color: #65415d;
        }

        [data-testid="stExpander"] summary {
            padding: 13px 16px;
            color: #eaddeb;
            font-weight: 650;
        }

        [data-testid="stExpander"] details {
            border: none;
        }

        /* =========================================
           DATAFRAMES AND TABLES
        ========================================= */

        [data-testid="stDataFrame"],
        [data-testid="stTable"] {
            border: 1px solid #3c2d45;
            border-radius: 14px;
            overflow: hidden;
            background: rgba(20, 16, 27, 0.85);
        }

        [data-testid="stDataFrame"] [role="grid"] {
            border: none;
        }

        [data-testid="stDataFrame"] [role="columnheader"] {
            background: #241b2e !important;
            color: #f0ddec !important;
            font-weight: 700;
        }

        [data-testid="stDataFrame"] [role="gridcell"] {
            border-color: rgba(100, 75, 112, 0.24);
        }

        [data-testid="stDataFrame"] [role="gridcell"]:hover {
            background: rgba(240, 128, 183, 0.07);
        }

        /* =========================================
           CHARTS AND IMAGES
        ========================================= */

        [data-testid="stPlotlyChart"],
        [data-testid="stImage"] {
            border: 1px solid #37283f;
            border-radius: 16px;
            overflow: hidden;
        }

        [data-testid="stArrowVegaLiteChart"],
        [data-testid="stVegaLiteChart"] {
            border-radius: 14px;
        }

        /* =========================================
           NOTICES AND STATUS MESSAGES
        ========================================= */

        [data-testid="stAlert"] {
            background: rgba(30, 23, 39, 0.94);
            border: 1px solid #49344f;
            border-radius: 13px;
            color: #e9dceF;
        }

        [data-testid="stAlert"] p {
            color: #e2d5e9;
        }

        [data-testid="stNotification"] {
            border-radius: 12px;
        }

        /* =========================================
           CODE, CAPTIONS AND DIVIDERS
        ========================================= */

        code {
            color: #f3a5d0 !important;
            background: #211827 !important;
            border-radius: 5px;
            padding: 2px 5px;
        }

        pre {
            border: 1px solid #44334d;
            border-radius: 13px;
        }

        [data-testid="stCaptionContainer"] p {
            color: #95869f !important;
            font-size: 0.82rem;
        }

        hr {
            border: none;
            height: 1px;
            background: linear-gradient(
                90deg,
                transparent,
                #67405f,
                #483858,
                transparent
            );
            margin: 1.7rem 0;
        }

        /* =========================================
           MULTI-COLUMN SPACING
        ========================================= */

        [data-testid="stHorizontalBlock"] {
            gap: 1rem;
        }

        /* Give spacing to main content sections */
        [data-testid="stVerticalBlock"] > [data-testid="stVerticalBlockBorderWrapper"] {
            border-radius: 16px;
        }

        /* =========================================
           SCROLLBAR
        ========================================= */

        ::-webkit-scrollbar {
            width: 9px;
            height: 9px;
        }

        ::-webkit-scrollbar-track {
            background: #100d15;
        }

        ::-webkit-scrollbar-thumb {
            background: #49334e;
            border-radius: 999px;
        }

        ::-webkit-scrollbar-thumb:hover {
            background: #86517d;
        }

        /* =========================================
           RESPONSIVE DESIGN
        ========================================= */

        @media (max-width: 768px) {
            .block-container {
                padding: 1.3rem 1rem 2.5rem;
            }

            .hero-card {
                padding: 24px 21px;
                border-radius: 18px;
            }

            .hero-card h1 {
                font-size: 2.25rem !important;
            }

            [data-testid="stMetric"] {
                padding: 15px;
                min-height: auto;
            }

            [data-testid="stMetricValue"] {
                font-size: 1.4rem !important;
            }
        }

        /* Respect reduced-motion preferences */
        @media (prefers-reduced-motion: reduce) {
            *,
            *::before,
            *::after {
                scroll-behavior: auto !important;
                transition-duration: 0.01ms !important;
                animation-duration: 0.01ms !important;
            }
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
