import math
from datetime import datetime
import streamlit as st
import streamlit.components.v1 as components

# ============================================================
# GUIA INGE - CONFIGURACION GENERAL DE LA APP
# ============================================================
st.set_page_config(page_title="Calculo en canales abiertos - Manning", page_icon="💧", layout="wide")
G = 9.81

# ============================================================
# GUIA INGE - DISEÑO VISUAL / COLORES / ESTILOS CSS
# Aqui se controla el color de fondo, tarjetas, botones, textos, etc.
# ============================================================
st.markdown("""
<style>
:root{
    --bg:#EEF3F8;
    --card:#FFFFFF;
    --nav:#0F172A;
    --text:#0F172A;
    --muted:#64748B;
    --accent:#2563EB;
    --accent2:#0EA5E9;
    --border:#CBD5E1;
    --input:#F8FAFC;
    --sidebar-btn:#38BDF8;
    --sidebar-btn-hover:#7DD3FC;
    --sidebar-btn-text:#0F172A;
}
html, body, [data-testid="stAppViewContainer"]{background:var(--bg) !important;color:var(--text) !important;}
[data-testid="stHeader"]{background:rgba(238,243,248,.88) !important;backdrop-filter:blur(10px);}
[data-testid="stSidebar"]{background:var(--nav) !important;border-right:1px solid rgba(255,255,255,.08);}
[data-testid="stSidebar"] h1,[data-testid="stSidebar"] h2,[data-testid="stSidebar"] h3,[data-testid="stSidebar"] p,[data-testid="stSidebar"] span,[data-testid="stSidebar"] label,[data-testid="stSidebar"] label p{color:#F8FAFC !important;}
[data-testid="stSidebar"] small,[data-testid="stSidebar"] .stMarkdown{color:#CBD5E1 !important;}
[data-testid="stMain"] p,[data-testid="stMain"] span,[data-testid="stMain"] label,[data-testid="stMain"] label p,[data-testid="stMain"] div[data-testid="stMarkdownContainer"] p{color:var(--text) !important;}
[data-testid="stMain"] .stTextInput label p,[data-testid="stMain"] .stNumberInput label p,[data-testid="stMain"] .stSelectbox label p{color:#1E293B !important;font-weight:700 !important;font-size:.96rem !important;}
[data-testid="stMain"] div[data-baseweb="input"],[data-testid="stMain"] div[data-baseweb="input"] > div{background:var(--input) !important;border:1.8px solid #9AA4AE !important;border-radius:14px !important;box-shadow:none !important;}
[data-testid="stMain"] div[data-baseweb="input"] input,[data-testid="stMain"] input{color:#0F172A !important;-webkit-text-fill-color:#0F172A !important;background:var(--input) !important;caret-color:#2563EB !important;}
[data-testid="stMain"] input::placeholder{color:#94A3B8 !important;-webkit-text-fill-color:#94A3B8 !important;}
[data-testid="stMain"] div[data-baseweb="select"] > div{background:#3B92D0 !important;border:0 !important;border-radius:14px !important;color:white !important;}
[data-testid="stMain"] div[data-baseweb="select"] span,[data-testid="stMain"] div[data-baseweb="select"] svg{color:white !important;fill:white !important;}
[data-testid="stSidebar"] div[data-baseweb="select"] > div{background:#111827 !important;border:1px solid #334155 !important;border-radius:12px !important;color:#F8FAFC !important;}
[data-testid="stSidebar"] div[data-baseweb="select"] span,[data-testid="stSidebar"] div[data-baseweb="select"] svg{color:#F8FAFC !important;fill:#F8FAFC !important;}
.stButton > button{border-radius:14px !important;font-weight:800 !important;border:0 !important;min-height:44px !important;box-shadow:0 6px 16px rgba(15,23,42,.10);}

/* ============================================================
   CAMBIO PEDIDO:
   Botones del panel izquierdo en color celeste y texto visible.
   Esto arregla "Cargar ejemplo" y "Limpiar cálculo".
   ============================================================ */
[data-testid="stSidebar"] .stButton > button{
    background:linear-gradient(135deg, #7DD3FC, #38BDF8) !important;
    color:var(--sidebar-btn-text) !important;
    border:1px solid rgba(186,230,253,.85) !important;
    box-shadow:0 8px 20px rgba(14,165,233,.25) !important;
}
[data-testid="stSidebar"] .stButton > button p,
[data-testid="stSidebar"] .stButton > button span,
[data-testid="stSidebar"] .stButton > button div{
    color:var(--sidebar-btn-text) !important;
    -webkit-text-fill-color:var(--sidebar-btn-text) !important;
    font-weight:900 !important;
}
[data-testid="stSidebar"] .stButton > button:hover{
    background:linear-gradient(135deg, #BAE6FD, #7DD3FC) !important;
    color:#0F172A !important;
    transform:translateY(-1px);
}
[data-testid="stSidebar"] .stButton > button:hover p,
[data-testid="stSidebar"] .stButton > button:hover span,
[data-testid="stSidebar"] .stButton > button:hover div{
    color:#0F172A !important;
    -webkit-text-fill-color:#0F172A !important;
}
[data-testid="stSidebar"] .stButton > button:active{transform:translateY(0);}

.main-title{font-size:2.55rem;font-weight:800;color:#0F172A;margin-bottom:.15rem;letter-spacing:-.035em;}
.main-subtitle{font-size:1.02rem;color:#64748B;margin-bottom:1rem;}
.card{background:#FFFFFF;border:1px solid rgba(219,228,239,.82);border-radius:24px;padding:1.45rem 1.6rem;box-shadow:0 12px 32px rgba(15,23,42,.055);margin-bottom:1rem;}
.card-title{color:#1D4ED8;font-size:1.45rem;font-weight:800;margin-bottom:1rem;letter-spacing:-.02em;}
.metric-grid{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:.85rem;}
.metric-box{background:#F8FAFC;border:1px solid #E2E8F0;border-radius:18px;padding:1rem;min-height:110px;}
.metric-label{font-size:.88rem;color:#64748B !important;font-weight:700;}
.metric-value{font-size:1.65rem;font-weight:800;color:#0F172A !important;margin-top:.15rem;}
.metric-unit{font-size:.82rem;color:#64748B !important;margin-top:.05rem;}
.flow-box{background:linear-gradient(135deg,#DBEAFE,#ECFEFF);border:1px solid #BFDBFE;border-radius:18px;padding:1rem 1.2rem;margin-top:.85rem;display:flex;justify-content:space-between;align-items:center;}
.flow-label{font-size:.98rem;color:#075985 !important;font-weight:800;}.flow-value{font-size:1.2rem;color:#0F172A !important;font-weight:800;}
.equation-box{background:#F8FAFC;border-left:5px solid #2563EB;border-radius:14px;padding:1rem 1.15rem;color:#0F172A !important;line-height:1.65;font-family:Consolas,monospace;font-size:.92rem;white-space:pre-wrap;}
.small-note{color:#64748B !important;font-size:.9rem;margin-top:.5rem;}.section-pill{display:inline-block;padding:.42rem .75rem;border-radius:999px;background:#DBEAFE;color:#1E40AF !important;font-weight:800;font-size:.9rem;margin-bottom:.85rem;}
.footer-text{text-align:center;color:#64748B !important;font-size:.85rem;margin-top:1.2rem;}
@media(max-width:1100px){.metric-grid{grid-template-columns:repeat(2,minmax(0,1fr));}}@media(max-width:700px){.metric-grid{grid-template-columns:1fr}.main-title{font-size:2rem}}
</style>
""", unsafe_allow_html=True)

# ============================================================
# GUIA INGE - CONVERSIONES DE UNIDADES
# Aqui se convierten caudal, pendiente y longitudes al Sistema Internacional.
# ============================================================
def convert_q_to_m3s(value, unit):
    return value if unit == "m³/s" else value/1000 if unit == "L/s" else value*0.0283168466

def convert_s_to_m_m(value, unit):
    return value if unit == "m/m" else value/100

def convert_length_to_m(value, unit):
    return value if unit == "m" else value/100 if unit == "cm" else value/1000 if unit == "mm" else value*0.3048

# ============================================================
# GUIA INGE - ECUACION MANNING
# Formula principal:
# Q = (1/n) A R^(2/3) S^(1/2)
# R = A/P
# ============================================================
def manning_q(A, R, n, S):
    return (1/n) * A * (R ** (2/3)) * math.sqrt(S)

def classify_flow(F):
    if abs(F-1) <= 0.01:
        return "Crítico"
    return "Subcrítico" if F < 1 else "Supercrítico"

# ============================================================
# GUIA INGE - GEOMETRIA HIDRAULICA DE LAS SECCIONES
# Aqui estan las ecuaciones de area A, perimetro mojado P,
# radio hidraulico R, espejo de agua T y profundidad hidraulica Dh.
# ============================================================
def geom_rectangular(y, b):
    A = b*y
    P = b + 2*y
    R = A/P
    T = b
    Dh = A/T
    return A, P, R, T, Dh

def geom_trapezoidal(y, b, z):
    A = (b + z*y)*y
    P = b + 2*y*math.sqrt(1+z**2)
    R = A/P
    T = b + 2*z*y
    Dh = A/T
    return A, P, R, T, Dh

def geom_triangular(y, z):
    A = z*y**2
    P = 2*y*math.sqrt(1+z**2)
    R = A/P
    T = 2*z*y
    Dh = A/T
    return A, P, R, T, Dh

def geom_circular(y, D):
    if y <= 0 or y >= D:
        raise ValueError("En sección circular, el tirante debe estar entre 0 y el diámetro.")
    theta = 2 * math.acos(1 - 2*y/D)
    A = ((theta - math.sin(theta))*D**2)/8
    P = theta*D/2
    R = A/P
    T = 2*math.sqrt(y*(D-y))
    Dh = A/T
    return A, P, R, T, Dh

# ============================================================
# GUIA INGE - CALCULO DE CAUDAL PARA UN TIRANTE y
# Esta funcion calcula Q para una profundidad y propuesta.
# Luego se compara contra el Q ingresado por el usuario.
# ============================================================
def q_depth(section, y, n, S, b=0, z=0, D=0):
    if section == "Rectangular":
        A, P, R, T, Dh = geom_rectangular(y, b)
    elif section == "Trapezoidal":
        A, P, R, T, Dh = geom_trapezoidal(y, b, z)
    elif section == "Triangular":
        A, P, R, T, Dh = geom_triangular(y, z)
    else:
        A, P, R, T, Dh = geom_circular(y, D)
    return manning_q(A, R, n, S)

# ============================================================
# GUIA INGE - METODO NUMERICO BISECCION
# Se usa porque el tirante y aparece dentro de A, P y R.
# La app busca el valor de y que hace que:
# q_depth(y) - Q = 0
# ============================================================
def bisection(func, a, b, tol=1e-8, max_iter=220):
    fa, fb = func(a), func(b)

    if fa*fb > 0:
        return None

    for _ in range(max_iter):
        c = (a+b)/2
        fc = func(c)

        if abs(fc) < tol or abs(b-a) < tol:
            return c

        if fa*fc < 0:
            b, fb = c, fc
        else:
            a, fa = c, fc

    return (a+b)/2

# ============================================================
# GUIA INGE - CALCULO TIRANTE EN SECCION CIRCULAR
# En tuberia/canal circular puede haber mas de una raiz.
# Por eso se recorre el intervalo entre 0 y D.
# ============================================================
def solve_circular(Q, n, S, D):
    def f(y):
        return q_depth("Circular", y, n, S, D=D) - Q

    ymin, ymax, steps = 0.0001*D, 0.9999*D, 1000
    prev_y, prev_f = ymin, f(ymin)
    roots = []

    for i in range(1, steps+1):
        y = ymin + (ymax-ymin)*i/steps
        fy = f(y)

        if prev_f*fy < 0:
            root = bisection(f, prev_y, y)
            if root is not None:
                roots.append(root)

        prev_y, prev_f = y, fy

    if not roots:
        raise ValueError("No se encontró tirante normal. Verifique si el diámetro es suficiente para el caudal.")

    return min(roots)

# ============================================================
# GUIA INGE - CALCULO TIRANTE NORMAL
# Esta funcion resuelve el tirante normal y para cualquier seccion.
# ============================================================
def solve_depth(section, Q, n, S, b=0, z=0, D=0):
    if section == "Circular":
        return solve_circular(Q, n, S, D)

    def f(y):
        return q_depth(section, y, n, S, b=b, z=z, D=D) - Q

    ymin, ymax = 1e-6, 1

    while f(ymax) < 0:
        ymax *= 2
        if ymax > 10000:
            raise ValueError("No se encontró un rango válido para el tirante normal.")

    root = bisection(f, ymin, ymax)

    if root is None:
        raise ValueError("No se pudo resolver el tirante normal.")

    return root

# ============================================================
# GUIA INGE - RESULTADOS HIDRAULICOS FINALES
# Aqui se calcula:
# y, A, P, R, T, Dh, V, Froude, Energia especifica y tipo de flujo.
# ============================================================
def calculate(section, Q, n, S, b=0, z=0, D=0):
    y = solve_depth(section, Q, n, S, b, z, D)

    if section == "Rectangular":
        A, P, R, T, Dh = geom_rectangular(y, b)
    elif section == "Trapezoidal":
        A, P, R, T, Dh = geom_trapezoidal(y, b, z)
    elif section == "Triangular":
        A, P, R, T, Dh = geom_triangular(y, z)
    else:
        A, P, R, T, Dh = geom_circular(y, D)

    V = Q/A
    F = V/math.sqrt(G*Dh)
    E = y + V**2/(2*G)

    return {
        "y": y,
        "A": A,
        "P": P,
        "R": R,
        "T": T,
        "Dh": Dh,
        "V": V,
        "F": F,
        "E": E,
        "type": classify_flow(F),
        "Q_calc": manning_q(A, R, n, S)
    }

# ============================================================
# GUIA INGE - DIBUJOS SVG DE LAS SECCIONES
# Esta parte solo dibuja la vista conceptual del canal.
# No afecta los calculos hidraulicos.
# ============================================================
def clamp(v, a, b):
    return max(a, min(b, v))

def svg(section, result=None, D=1):
    if result:
        ratio = result["y"]/D if section == "Circular" and D > 0 else result["y"]/(result["y"]+1)
    else:
        ratio = 0.55

    ratio = clamp(ratio, 0.10, 0.90)

    bg = '<rect x="0" y="0" width="680" height="360" rx="22" fill="#dbeafe"/><circle cx="100" cy="78" r="58" fill="#bfdbfe"/><circle cx="590" cy="265" r="58" fill="#bfdbfe"/>'

    common = '''
    <style>
    .water{
        animation:wave 3.8s ease-in-out infinite alternate;
        transform-origin:center;
    }
    @keyframes wave{
        0%{transform:translateY(0);opacity:.92}
        100%{transform:translateY(-6px);opacity:.98}
    }
    .label{
        font:700 28px Segoe UI,Arial;
        fill:#0f172a;
    }
    .thin{
        stroke:#fff;
        stroke-width:4;
        stroke-linecap:round;
        opacity:.92;
    }
    </style>
    '''

    if section == "Trapezoidal":
        wy = 260 - ratio*140
        lx = 166 + (wy-90)*0.62
        rx = 514 - (wy-90)*0.62

        body = f'''
        {bg}
        <polygon points="130,80 250,290 430,290 550,80" fill="#cbd5e1" stroke="#0f172a" stroke-width="7" stroke-linejoin="round"/>
        <polygon class="water" points="{lx},{wy} 250,260 430,260 {rx},{wy}" fill="#2563eb"/>
        <path class="thin" d="M {lx} {wy} C 245 {wy-9}, 355 {wy+9}, {rx} {wy}" fill="none"/>
        <text class="label" x="335" y="66" text-anchor="middle">T</text>
        <text class="label" x="340" y="323" text-anchor="middle">b</text>
        <text class="label" x="554" y="206">y</text>
        <text class="label" x="205" y="212">Z</text>
        '''

    elif section == "Triangular":
        wy = 285 - ratio*170
        lx = 340 - (285-wy)*0.72
        rx = 340 + (285-wy)*0.72

        body = f'''
        {bg}
        <polygon points="145,80 340,302 535,80" fill="#cbd5e1" stroke="#0f172a" stroke-width="7" stroke-linejoin="round"/>
        <polygon class="water" points="{lx},{wy} 340,270 {rx},{wy}" fill="#2563eb"/>
        <path class="thin" d="M {lx} {wy} C 270 {wy-9}, 410 {wy+9}, {rx} {wy}" fill="none"/>
        <text class="label" x="335" y="65" text-anchor="middle">T</text>
        <text class="label" x="550" y="206">y</text>
        <text class="label" x="205" y="215">Z</text>
        '''

    elif section == "Rectangular":
        wy = 285 - ratio*180

        body = f'''
        {bg}
        <rect x="195" y="85" width="290" height="205" fill="#cbd5e1" stroke="#0f172a" stroke-width="7"/>
        <rect class="water" x="218" y="{wy}" width="244" height="{285-wy}" fill="#2563eb"/>
        <path class="thin" d="M 218 {wy} C 285 {wy-8}, 395 {wy+8}, 462 {wy}" fill="none"/>
        <text class="label" x="340" y="64" text-anchor="middle">b = T</text>
        <text class="label" x="505" y="205">y</text>
        '''

    else:
        wy = 287 - ratio*204
        wh = 287-wy

        body = f'''
        {bg}
        <defs>
            <clipPath id="pipeClip">
                <circle cx="340" cy="185" r="112"/>
            </clipPath>
        </defs>
        <circle cx="340" cy="185" r="118" fill="#cbd5e1" stroke="#0f172a" stroke-width="7"/>
        <g clip-path="url(#pipeClip)">
            <rect class="water" x="210" y="{wy}" width="260" height="{wh}" fill="#2563eb"/>
            <path class="thin" d="M 220 {wy} C 280 {wy-8}, 400 {wy+8}, 460 {wy}" fill="none"/>
        </g>
        <circle cx="340" cy="185" r="118" fill="none" stroke="#0f172a" stroke-width="7"/>
        <text class="label" x="340" y="52" text-anchor="middle">T</text>
        <text class="label" x="190" y="190">D</text>
        <text class="label" x="500" y="190">y</text>
        '''

    return f'<svg viewBox="0 0 680 360" width="100%" height="320" xmlns="http://www.w3.org/2000/svg">{common}{body}</svg>'

# ============================================================
# GUIA INGE - ECUACIONES MOSTRADAS EN PANTALLA
# Estas son las formulas que aparecen en la tarjeta derecha.
# ============================================================
def equations(section):
    return {
        "Rectangular": "A = by\nP = b + 2y\nR = by/(b+2y)\nT = b",
        "Trapezoidal": "A = (b + Zy)y\nP = b + 2y√(1 + Z²)\nR = A/P\nT = b + 2Zy",
        "Triangular": "A = Zy²\nP = 2y√(1 + Z²)\nR = A/P\nT = 2Zy",
        "Circular": "θ = 2 arccos(1 - 2y/D)\nA = ((θ - senθ)D²)/8\nP = θD/2\nR = A/P\nT = 2√(y(D-y))"
    }[section]

# ============================================================
# GUIA INGE - PROCEDIMIENTO / REPORTE DESCARGABLE
# Aqui se arma el texto que se muestra y se descarga como reporte.
# ============================================================
def procedure(section, project, conv, result):
    lines = [
        "CALCULO EN CANALES ABIERTOS - MANNING",
        "="*62,
        "",
        f"Lugar: {project['Lugar']}",
        f"Tramo: {project['Tramo']}",
        f"Proyecto: {project['Proyecto']}",
        f"Revestimiento: {project['Revestimiento']}",
        f"Sección: {section}",
        "",
        "Ecuación de Manning:",
        "Q = (1/n) A R^(2/3) S^(1/2)",
        "R = A/P",
        "",
        "Datos convertidos al Sistema Internacional:",
        f"Q = {conv['Q']:.6f} m³/s",
        f"n = {conv['n']:.6f}",
        f"S = {conv['S']:.6f} m/m"
    ]

    if section in ["Rectangular", "Trapezoidal"]:
        lines.append(f"b = {conv['b']:.6f} m")

    if section in ["Trapezoidal", "Triangular"]:
        lines.append(f"Z = {conv['z']:.6f}")

    if section == "Circular":
        lines.append(f"D = {conv['D']:.6f} m")

    lines += [
        "",
        "Geometría usada:",
        equations(section),
        "",
        "Resultados finales:",
        f"y = {result['y']:.6f} m",
        f"A = {result['A']:.6f} m²",
        f"P = {result['P']:.6f} m",
        f"R = {result['R']:.6f} m",
        f"T = {result['T']:.6f} m",
        f"D_h = A/T = {result['Dh']:.6f} m",
        f"V = Q/A = {result['V']:.6f} m/s",
        f"F = V/√(gD_h) = {result['F']:.6f}",
        f"E = y + V²/(2g) = {result['E']:.6f} m",
        f"Q calculado = {result['Q_calc']:.6f} m³/s",
        f"Tipo de flujo = {result['type']}"
    ]

    return "\n".join(lines)

# ============================================================
# GUIA INGE - ESTADO DE LA APP
# Aqui Streamlit guarda resultados, procedimiento, seccion y datos convertidos.
# ============================================================
for key, default in {
    "result": None,
    "procedure": "",
    "section": "Trapezoidal",
    "conv": {},
    "example": False
}.items():
    if key not in st.session_state:
        st.session_state[key] = default

# ============================================================
# GUIA INGE - PANEL LATERAL
# Aqui estan los selectores de seccion, unidades y botones.
# ============================================================
with st.sidebar:
    st.markdown(
        '<div style="padding:1.2rem 0">'
        '<div style="font-size:2.1rem;font-weight:800;line-height:1.15;color:white">'
        'Manning<br>FlowLab'
        '</div>'
        '<div style="font-size:.98rem;color:#cbd5e1;margin-top:.9rem">'
        'Cálculo de tirante normal con procedimiento hidráulico'
        '</div>'
        '</div>',
        unsafe_allow_html=True
    )

    st.divider()

    section = st.selectbox(
        "Tipo de sección",
        ["Trapezoidal", "Triangular", "Circular", "Rectangular"],
        index=["Trapezoidal", "Triangular", "Circular", "Rectangular"].index(st.session_state.section)
    )

    st.session_state.section = section

    st.markdown("**Unidades**")

    q_unit = st.selectbox("Caudal", ["m³/s", "L/s", "ft³/s"])
    s_unit = st.selectbox("Pendiente", ["m/m", "%"], index=1)
    l_unit = st.selectbox("Longitudes", ["m", "cm", "mm", "ft"])

    st.divider()

    if st.button("Cargar ejemplo", use_container_width=True):
        st.session_state.example = True
        st.rerun()

    if st.button("Limpiar cálculo", use_container_width=True):
        st.session_state.result = None
        st.session_state.procedure = ""
        st.session_state.conv = {}
        st.session_state.example = False
        st.rerun()

# ============================================================
# GUIA INGE - TITULO PRINCIPAL
# ============================================================
st.markdown(
    '<div class="main-title">Calculo en canales abiertos - Manning</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="main-subtitle">'
    'Herramienta para determinar el tirante normal y los elementos hidráulicos de secciones de canal abierto.'
    '</div>',
    unsafe_allow_html=True
)

# ============================================================
# GUIA INGE - VALORES DE EJEMPLO
# Estos son los datos que se cargan al presionar "Cargar ejemplo".
# ============================================================
ex = st.session_state.example

proj_defaults = {
    "Lugar": "Urbanización Tela" if ex else "",
    "Tramo": "Canal de descarga" if ex else "",
    "Proyecto": "Drenaje pluvial" if ex else "",
    "Revestimiento": "Concreto" if ex else ""
}

input_defaults = {
    "Q": 0.33 if ex else 0.0,
    "n": 0.013 if ex else 0.0,
    "S": 1.25 if ex else 0.0,
    "b": 0.33 if ex else 0.0,
    "z": 0.5774 if ex else 0.0,
    "D": 0.60 if ex else 0.0
}

# ============================================================
# GUIA INGE - DATOS DEL PROYECTO
# ============================================================
st.markdown('<div class="card"><div class="card-title">Datos del proyecto</div>', unsafe_allow_html=True)

c1, c2 = st.columns(2)

with c1:
    lugar = st.text_input("Lugar", value=proj_defaults["Lugar"])
    tramo = st.text_input("Tramo", value=proj_defaults["Tramo"])

with c2:
    proyecto = st.text_input("Proyecto", value=proj_defaults["Proyecto"])
    revestimiento = st.text_input("Revestimiento", value=proj_defaults["Revestimiento"])

st.markdown('</div>', unsafe_allow_html=True)

# ============================================================
# GUIA INGE - ENTRADAS HIDRAULICAS Y VISTA CONCEPTUAL
# ============================================================
left, right = st.columns([1.45, 1], gap="large")

with left:
    st.markdown('<div class="card"><div class="card-title">Entradas hidráulicas</div>', unsafe_allow_html=True)

    Q_in = st.number_input(
        "Caudal Q",
        min_value=0.0,
        value=float(input_defaults["Q"]),
        step=0.01,
        format="%.6f"
    )

    n = st.number_input(
        "Rugosidad n",
        min_value=0.0,
        value=float(input_defaults["n"]),
        step=0.001,
        format="%.6f"
    )

    S_in = st.number_input(
        "Pendiente S",
        min_value=0.0,
        value=float(input_defaults["S"]),
        step=0.01,
        format="%.6f"
    )

    b_in = z = D_in = 0.0

    if section in ["Trapezoidal", "Rectangular"]:
        b_in = st.number_input(
            "Solera b",
            min_value=0.0,
            value=float(input_defaults["b"]),
            step=0.01,
            format="%.6f"
        )

    if section in ["Trapezoidal", "Triangular"]:
        z = st.number_input(
            "Talud Z (H:V)",
            min_value=0.0,
            value=float(input_defaults["z"]),
            step=0.01,
            format="%.6f"
        )

    if section == "Circular":
        D_in = st.number_input(
            "Diámetro D",
            min_value=0.0,
            value=float(input_defaults["D"]),
            step=0.01,
            format="%.6f"
        )

    st.markdown(
        '<div class="small-note">'
        'La pendiente puede ingresarse como porcentaje o como relación m/m, según la unidad seleccionada.'
        '</div>',
        unsafe_allow_html=True
    )

    calc_btn = st.button("Calcular", type="primary", use_container_width=True)

    st.markdown('</div>', unsafe_allow_html=True)

with right:
    st.markdown('<div class="card"><div class="card-title">Vista conceptual</div>', unsafe_allow_html=True)

    preview = st.session_state.result if st.session_state.section == section else None

    # IMPORTANTE:
    # Aqui se usa components.html para que el SVG salga como figura
    # y no como codigo de texto.
    components.html(
        svg(section, preview, D=st.session_state.conv.get("D", 1)),
        height=340
    )

    st.markdown(f'<div class="section-pill">{section}</div>', unsafe_allow_html=True)
    st.markdown('<div class="equation-box">' + equations(section) + '</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# ============================================================
# GUIA INGE - BOTON CALCULAR / VALIDACION / EJECUCION
# Aqui se convierten los datos, se validan y se llama calculate().
# ============================================================
if calc_btn:
    try:
        if Q_in <= 0:
            raise ValueError("El caudal debe ser mayor que cero.")

        if n <= 0:
            raise ValueError("La rugosidad debe ser mayor que cero.")

        if S_in <= 0:
            raise ValueError("La pendiente debe ser mayor que cero.")

        Q = convert_q_to_m3s(Q_in, q_unit)
        S = convert_s_to_m_m(S_in, s_unit)

        b = convert_length_to_m(b_in, l_unit) if section in ["Trapezoidal", "Rectangular"] else 0
        D = convert_length_to_m(D_in, l_unit) if section == "Circular" else 0

        if section in ["Trapezoidal", "Rectangular"] and b <= 0:
            raise ValueError("La solera b debe ser mayor que cero.")

        if section in ["Trapezoidal", "Triangular"] and z <= 0:
            raise ValueError("El talud Z debe ser mayor que cero.")

        if section == "Circular" and D <= 0:
            raise ValueError("El diámetro D debe ser mayor que cero.")

        result = calculate(section, Q, n, S, b=b, z=z, D=D)

        conv = {
            "Q": Q,
            "n": n,
            "S": S,
            "b": b,
            "z": z,
            "D": D
        }

        proj = {
            "Lugar": lugar,
            "Tramo": tramo,
            "Proyecto": proyecto,
            "Revestimiento": revestimiento
        }

        st.session_state.result = result
        st.session_state.conv = conv
        st.session_state.procedure = procedure(section, proj, conv, result)
        st.session_state.section = section

        st.success("Cálculo realizado correctamente.")

    except Exception as e:
        st.session_state.result = None
        st.session_state.procedure = ""
        st.error(str(e))

# ============================================================
# GUIA INGE - MOSTRAR RESULTADOS EN PANTALLA
# Aqui aparecen las tarjetas de y, A, P, R, T, V, F y E.
# ============================================================
result = st.session_state.result

if result is not None and st.session_state.section == section:
    st.markdown('<div class="card"><div class="card-title">Resultados</div>', unsafe_allow_html=True)

    st.markdown(f'''
    <div class="metric-grid">
      <div class="metric-box">
        <div class="metric-label">Tirante normal y</div>
        <div class="metric-value">{result['y']:.4f}</div>
        <div class="metric-unit">m</div>
      </div>

      <div class="metric-box">
        <div class="metric-label">Área hidráulica A</div>
        <div class="metric-value">{result['A']:.4f}</div>
        <div class="metric-unit">m²</div>
      </div>

      <div class="metric-box">
        <div class="metric-label">Perímetro mojado P</div>
        <div class="metric-value">{result['P']:.4f}</div>
        <div class="metric-unit">m</div>
      </div>

      <div class="metric-box">
        <div class="metric-label">Radio hidráulico R</div>
        <div class="metric-value">{result['R']:.4f}</div>
        <div class="metric-unit">m</div>
      </div>

      <div class="metric-box">
        <div class="metric-label">Espejo de agua T</div>
        <div class="metric-value">{result['T']:.4f}</div>
        <div class="metric-unit">m</div>
      </div>

      <div class="metric-box">
        <div class="metric-label">Velocidad V</div>
        <div class="metric-value">{result['V']:.4f}</div>
        <div class="metric-unit">m/s</div>
      </div>

      <div class="metric-box">
        <div class="metric-label">Número de Froude F</div>
        <div class="metric-value">{result['F']:.4f}</div>
        <div class="metric-unit">adimensional</div>
      </div>

      <div class="metric-box">
        <div class="metric-label">Energía específica E</div>
        <div class="metric-value">{result['E']:.4f}</div>
        <div class="metric-unit">m</div>
      </div>
    </div>

    <div class="flow-box">
        <div class="flow-label">Clasificación del flujo</div>
        <div class="flow-value">{result['type']}</div>
    </div>
    ''', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

    # ========================================================
    # GUIA INGE - PROCEDIMIENTO MOSTRADO Y DESCARGA DEL REPORTE
    # ========================================================
    st.markdown('<div class="card"><div class="card-title">Procedimiento</div>', unsafe_allow_html=True)

    st.code(st.session_state.procedure, language="text")

    st.download_button(
        "Descargar reporte",
        st.session_state.procedure.encode("utf-8"),
        file_name="reporte_manning_" + datetime.now().strftime("%Y%m%d_%H%M%S") + ".txt",
        mime="text/plain",
        use_container_width=True
    )

    st.markdown('</div>', unsafe_allow_html=True)

# ============================================================
# GUIA INGE - PIE DE PAGINA
# ============================================================
st.markdown(
    '<div class="footer-text">'
    'El tirante normal se obtiene mediante bisección, debido a que la profundidad aparece dentro de las expresiones geométricas de la sección.'
    '</div>',
    unsafe_allow_html=True
)