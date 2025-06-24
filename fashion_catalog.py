import random
import csv
from typing import List, Tuple, Dict
from collections import defaultdict
import heapq

def estimate_price(brand: str, piece: str) -> int:
    """Estimate price based on brand and item type."""
    brand_tiers = {
        'Balenciaga': 5, 'Off-White': 5, 'Rick Owens': 5, 'Yohji Yamamoto': 5,
        'Prada': 4, 'Acne Studios': 4, 'A-COLD-WALL*': 3,
        'COS': 2, 'Uniqlo': 1, 'Zara': 1
    }
    
    piece_types = {
        'shoes': 3, 'pants': 2, 'shirt': 1
    }
    
    # Base price calculation
    base_price = 100 * brand_tiers.get(brand, 1) * piece_types.get(piece.split()[0], 1)
    
    # Add premium for luxury brands
    if brand in ['Balenciaga', 'Off-White', 'Rick Owens', 'Yohji Yamamoto', 'Prada']:
        base_price *= 1.5
    
    return int(base_price)

def load_catalog(file_path: str) -> Dict[str, List[Tuple[str, str, int]]]:
    """Load fashion catalog from TSV file with estimated prices."""
    catalog = defaultdict(list)
    
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file, delimiter='\t')
        for row in reader:
            piece = row['Fashion Piece'].lower()
            brand = row['Brand']
            price = estimate_price(brand, piece)
            
            if 'shoe' in piece or 'boot' in piece or 'loafer' in piece:
                catalog['shoes'].append((piece, brand, price))
            elif 'pants' in piece or 'shorts' in piece or 'trousers' in piece or 'skirt' in piece:
                catalog['pants'].append((piece, brand, price))
            elif 'shirt' in piece or 'blouse' in piece or 'sweater' in piece or 'top' in piece:
                catalog['shirt'].append((piece, brand, price))
    
    return catalog

def generate_expensive_outfits(catalog: Dict[str, List[Tuple[str, str, int]]], name='Bowen', top_n=10):
    """Generate the top N most expensive outfit combinations."""
    # Generate all possible combinations
    combinations = []
    
    for shoe in catalog['shoes']:
        for pants in catalog['pants']:
            for shirt in catalog['shirt']:
                total_price = shoe[2] + pants[2] + shirt[2]
                outfit = (
                    f"{name} should wear {shoe[0]} from {shoe[1]}, {pants[0]} from {pants[1]}, and {shirt[0]} from {shirt[1]}",
                    total_price
                )
                combinations.append(outfit)
    
    # Get the top N most expensive combinations
    top_combinations = heapq.nlargest(top_n, combinations, key=lambda x: x[1])
    
    return top_combinations

if __name__ == "__main__":
    catalog = load_catalog('/Users/bowenyao/CascadeProjects/fashion_catalog.txt')
    expensive_outfits = generate_expensive_outfits(catalog)
    
    print("Top 10 Most Expensive Outfit Combinations:")
    for i, (outfit, price) in enumerate(expensive_outfits, 1):
        print(f"\n{i}. {outfit} (${price:,})")
