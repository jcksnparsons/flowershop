import sqlite3
from django.urls import reverse
from django.shortcuts import render, redirect
from bouquetapp.models import Bouquet, Flower
from ..connection import Connection

def create_bouquet(cursor, row):
    _row = sqlite3.Row(cursor,row)

    bouquet = Bouquet()
    bouquet.id = _row["id"]
    bouquet.name = _row["bouquet_name"]
    bouquet.occasion = _row["occasion"]
    bouquet.flowersWithQuantity = []
    
    flower = Flower()
    flower.id = _row["flower_id"]
    flower.name = _row["flower_name"]
    flower.quantity = _row["quantity"]

    return (bouquet, flower,)


def get_bouquet(bouquet_id):
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = create_bouquet
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            b.id,
            b.name AS bouquet_name,
            b.occasion,
            f.id AS flower_id,
            f.name AS flower_name,
            bf.quantity
        FROM bouquetapp_bouquet b
        LEFT JOIN bouquetapp_bouquetflower bf ON b.id = bf.bouquet_id
        LEFT JOIN bouquetapp_flower f ON f.id = bf.flower_id
        WHERE b.id = ?
        """,(bouquet_id,))

        data = db_cursor.fetchall()

        bouquet_groups = {}

        for (bouquet, flower) in data:

            if bouquet.id not in bouquet_groups:
                bouquet_groups[bouquet.id] = bouquet
                bouquet_groups[bouquet.id].flowersWithQuantity.append(flower)

            else:
                bouquet_groups[bouquet.id].flowersWithQuantity.append(flower)

        return bouquet_groups[bouquet.id]

def bouquet_details(request, bouquet_id):
    if request.method == 'GET':
        bouquet = get_bouquet(bouquet_id)

        template = 'bouquets/detail.html'
        context = {
            'bouquet': bouquet
        }

        return render(request, template, context)