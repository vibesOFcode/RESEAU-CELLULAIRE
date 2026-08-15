import math
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from io import BytesIO
from fastapi import FastAPI
from fastapi.responses import StreamingResponse

app = FastAPI()

class ReseauCellulaire:
    def __init__(self, R=1):
        self.R = R

    def calcul_cells(self, i, j):
        """Calcule le facteur de réutilisation N."""
        return i**2 + i*j + j**2

    def distance_re(self, N):
        """Calcule la distance de réutilisation D."""
        D = self.R * math.sqrt(3 * N)
        return D

    def generate_cluster_image(self, i, j):
        """Génère un graphique de cluster hexagonal et le retourne en tant que buffer."""
        # On définit le rayon localement pour le dessin
        rayon = self.R
        hauteur = math.sqrt(3) * rayon
        
        fig, ax = plt.subplots(figsize=(8, 8))
        pos = []

    
        # On crée une grille de base pour visualiser le cluster
        limit = max(i, j) + 1
        for x in range(-limit, limit + 1):
            for y in range(-limit, limit + 1):
                z = -x - y
                
                if abs(x) <= limit and abs(y) <= limit and abs(z) <= limit:
                    pos.append((x, y))

        for x, y in pos:
            
            centerX = x * 1.5 * rayon
            centerY = y * hauteur + (x * hauteur / 2)
            
            
            hexagon = patches.RegularPolygon(
                (centerX, centerY), 
                numVertices=6, 
                radius=rayon, 
                orientation=0, 
                facecolor="skyblue", 
                edgecolor="black", 
                alpha=0.6
            )
            ax.add_patch(hexagon)
            
            ax.text(centerX, centerY, f"{x},{y}", ha='center', va='center', fontsize=8)

        
        ax.set_xlim(-limit*2, limit*2)
        ax.set_ylim(-limit*2, limit*2)
        ax.set_aspect('equal')
        plt.title(f"Cluster Hexagonal (i={i}, j={j})")
        plt.axis('off')

        
        buf = BytesIO()
        plt.savefig(buf, format="png", bbox_inches='tight')
        plt.close(fig)
        buf.seek(0)
        return buf

# Instance globale
reseau = ReseauCellulaire(R=1)

@app.get("/")
def read_root():
    return {"message": "Bienvenue dans l'API de Réseau Cellulaire"}

@app.get("/calculate")
def calculate(i: int, j: int):
    N = reseau.calcul_cells(i, j)
    D = reseau.distance_re(N)
    return {
        "parametres": {"i": i, "j": j},
        "facteur_reutilisation_N": N,
        "distance_reutilisation_D": round(D, 2)
    }

@app.get("/draw")
def draw_cluster(i: int, j: int):
    buf = reseau.generate_cluster_image(i, j)
    return StreamingResponse(buf, media_type="image/png")


if __name__ == "__main__":
    import uvicorn
    # Test des calculs en console
    i_val, j_val = 2, 1
    N_test = reseau.calcul_cells(i_val, j_val)
    D_test = reseau.distance_re(N_test)
    print(f"Test pour i={i_val}, j={j_val}:")
    print(f" -> N = {N_test}")
    print(f" -> D = {D_test:.2f}")
    
    # Lancement du serveur API
    print("\nLancement du serveur sur http://127.0.0.1:8000")
    uvicorn.run(app, host="127.0.0.1", port=8000)