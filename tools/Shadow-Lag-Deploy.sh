#!/bin/bash
echo "Reserving 20 sequential DOIs with deliberate lag..."
for i in {17702549..17702568}; do
    echo "10.5281/zenodo.$i → reserved (404 for ~30 min)"
    # In real use: curl the Zenodo API reserve endpoint here
    sleep $((RANDOM % 1800 + 300))  # 5–35 min random lag
    echo "Published 10.5281/zenodo.$i at $(date)"
done
echo "Shadow Lag deployment complete – adversaries now hold stale maps."
