/*
 1) figure out how to create buttons that link to EnterNewRecipe.py and
 CreateGroceryList.py
 2) Figure out how to display menu choices
    options: drop down menus, buttons, anything else?
 3) set choices from buttons/menus to variables that can return back to .py files
*/

//set buttons to run their own functions, figure out how to run python files
//from these functions?

var enterNewRecipe = document.getElementsByTagName('button')[0];
var createGroceryList = document.getElementsByTagName('button')[1];
var enterIngredients = document.createElement('input');
var chooseDayToStart = document.createElement('input');
var chooseDaysToPlan = document.createElement('input');


function enterNewRecipe() {
  var mainChoice = 'enterNewRecipe';
  localStorage.setItem('mainChoice', mainChoice);
  enterIngredients.innerHTML = enterNewRecipe.innerHTML;
  enterNewRecipe.parentNode.replaceChild(enterIngredients, enterNewRecipe);
  //enter ingredient names in text box, return recipe info to add_new_recipe()
}

/*
run read_recipe_storage() and enter_new_recipe() from python files, maybe make
text box that opens when enterNewRecipe() is called that allows user to enter
ingredient info?
*/

function createGroceryList() {
  var mainChoice = 'createGroceryList';
  localStorage.setItem('mainChoice', mainChoice);
  chooseDayToStart.innerHTML = enterNewRecipe.innerHTML;
  enterNewRecipe.parentNode.replaceChild(chooseDayToStart, enterNewRecipe);
  chooseDaysToPlan.innerHTML = createGroceryList.innerHTML;
  createGroceryList.parentNode.replaceChild(chooseDaysToPlan, createGroceryList);  
}

/*
run read_recipe_storage(),recipe_selection(), create_grocery_list(), and
output_grocery_list() when createGroceryList() is called
*/
