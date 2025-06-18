from server.app import create_my_app
from server.models import db, Restaurant, Pizza, RestaurantPizza

app = create_my_app()

with app.app_context():
    Pizza.query.delete()
    RestaurantPizza.query.delete()
    
    print("Chill one Sec..... ")

    # Clear existing data (optional)
    Restaurant.query.delete()
    Pizza.query.delete()
    RestaurantPizza.query.delete()

    # Create Restaurants
    r1 = Restaurant(name="Mama Mia", address="123 Pizza St")
    r2 = Restaurant(name="Papa's Pizzeria", address="456 Cheese Ave")
    db.session.add_all([r1, r2])

    # Create Pizzas
    p1 = Pizza(name="Margherita", ingredients="Tomato, Mozzarella, Basil")
    p2 = Pizza(name="Pepperoni", ingredients="Tomato, Cheese, Pepperoni")
    db.session.add_all([p1, p2])

    # Create RestaurantPizzas
    rp1 = RestaurantPizza(price=10.0, restaurant=r1, pizza=p1)
    rp2 = RestaurantPizza(price=12.5, restaurant=r1, pizza=p2)
    rp3 = RestaurantPizza(price=11.0, restaurant=r2, pizza=p1)
    db.session.add_all([rp1, rp2, rp3])

    db.session.commit()
    print("Done seeding!")
