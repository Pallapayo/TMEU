# TMEU — Topological Medium Effective Unification

Código completo y reproducible del artículo  
**"Origen Topológico de las Masas de Leptones Cargados y Hadrón Ligero en un Medio Estructural Universal (TMEU)"**  
Jorge Granda García — 10 diciembre 2025

Reproduce:
- Electrón (w=1) → E_struct = 51.97
- Muón (w=14), Tau (w=59), Protón (w=43)
- α ≈ 1/137.1 emergente
- Dispersión e-e (Rutherford)
- Vida media del muón
- Fotón estructural, reconexión, g-2, etc.

Requisitos: Python 3.9+, numpy, scipy, matplotlib

```bash
pip install -r requirements.txt
python soliton_static.py --w 1     # electrón
python soliton_static.py --w 43    # protón
python scattering_ee.py            # α ≈ 1/137.1