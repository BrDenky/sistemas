#!/usr/bin/env python3
# amdahl_lab.py — Cumple los 4 puntos del laboratorio

import os
import argparse
import numpy as np

# Usar backend "Agg" para poder guardar la imagen sin entorno gráfico
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

def speedup(p: int, f: float) -> float:
    """Amdahl: S(p) = 1 / ((1 - f) + f/p)"""
    return 1.0 / ((1.0 - f) + (f / p))

def main():
    parser = argparse.ArgumentParser(description="Amdahl's Law lab")
    parser.add_argument("--f", type=float, default=0.8,
                        help="Parallel fraction f (default: 0.8)")
    parser.add_argument("--pmax", type=int, default=os.cpu_count() or 1,
                        help="Max processors to plot (default: CPU count)")
    parser.add_argument("--out", default="amdahl_speedup.png",
                        help="Output figure filename (PNG)")
    args = parser.parse_args()

    p_vals = np.arange(1, args.pmax + 1)
    S = np.array([speedup(p, args.f) for p in p_vals])

    # 1) Imprime tabla con eficiencia (S/p)
    print("p\tS(p)\t\tEfficiency S(p)/p")
    for p, s in zip(p_vals, S):
        print(f"{p}\t{s:.6f}\t{s/p:.6f}")

    # 2) Guarda la gráfica del speedup
    plt.figure(figsize=(7,5))
    plt.plot(p_vals, S, marker="o", label=f"Amdahl f={args.f}")
    plt.plot(p_vals, p_vals, "--", label="Ideal linear")
    plt.xlabel("Processors p")
    plt.ylabel("Speedup S(p)")
    plt.title("Amdahl's Law Speedup")
    plt.legend()
    plt.grid(True, linestyle=":")
    plt.tight_layout()
    plt.savefig(args.out, dpi=150)
    print(f"\n[OK] Saved plot to {args.out}")

    # 3) ¿Lineal o no? (chequeo simple de rendimientos decrecientes)
    diffs = np.diff(S)            # incrementos S(p)-S(p-1)
    concave = np.all(np.diff(diffs) < 0)
    max_theoretical = 1.0 / (1.0 - args.f)
    msg = "NOT linear; decreasing marginal returns (concave curve)" if concave else "Nonlinear"
    print(f"\nLinearity: {msg}. Theoretical max speedup = {max_theoretical:.4f}x")


if __name__ == "__main__":
    main()
