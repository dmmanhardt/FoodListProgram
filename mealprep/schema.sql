DROP TABLE IF EXISTS recipe;

CREATE TABLE recipe (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  recipe_name TEXT UNIQUE NOT NULL,
  meal_served TEXT NOT NULL,
  serving_size INTEGER NOT NULL,
  recipe_ingredients LIST NOT NULL,
  recipe_measurements LIST NOT NULL,
  recipe_amounts LIST NOT NULL
);
