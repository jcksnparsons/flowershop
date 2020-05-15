import sqlite3
from django.shortcuts import render, redirect, reverse
from bouquetapp.models import Bouquet
from ..connection import Connection

def bouquet_list(request):
    if request.method == 'GET':
        with sqlite3.connect(Connection.db_path) as conn:
            conn.row_factory = sqlite3.Row
            db_cursor = conn.cursor()

            db_cursor.execute("""
            SELECT
                b.id,
                b.name,
                b.occasion
            FROM bouquetapp_bouquet b
            ORDER BY b.name ASC;
            """)

            all_bouquets = []
            dataset = db_cursor.fetchall()

            for row in dataset:
                bouquet = Bouquet()
                bouquet.id = row["id"]
                bouquet.name = row["name"]
                bouquet.occasion = row["occasion"]

                all_bouquets.append(bouquet)

        template = 'bouquets/list.html'
        context = {
            'all_bouquets': all_bouquets
        }

        return render(request, template, context)

    elif request.method == 'POST':
        form_data = request.POST

        with sqlite3.connect(Connection.db_path) as conn:
            db_cursor = conn.cursor()

            db_cursor.execute("""
            INSERT INTO bouquetapp_bouquet
            (
                name, occasion
            )
            VALUES (?,?)
            """,
            (form_data["name"], form_data["occasion"]))

        return redirect(reverse('bouquetapp:home'))
                