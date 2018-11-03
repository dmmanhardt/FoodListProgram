/*
 1) figure out how to create buttons that link to EnterNewRecipe.py and
 CreateGroceryList.py
 2) Figure out how to display menu choices
    options: drop down menus, buttons, anything else?
 3) set choices from buttons/menus to variables that can return back to .py files
*/

//set buttons to run their own functions, figure out how to run python files
//from these functions?

var enterNewRecipe = document.getElementById('enterNewRecipe');
var createGroceryList = document.getElementById('createGroceryList');
var enterIngredients = document.createElement('input');
var chooseDayToStart = document.createElement('input');
var chooseDaysToPlan = document.createElement('input');

function replaceNewRecipeButton(mainChoice) {
  if (mainChoice === 'enterNewRecipe') {
    enterIngredients.innerHTML = enterNewRecipe.innerHTML;
    enterNewRecipe.parentNode.replaceChild(enterIngredients, enterNewRecipe);
  } else if (mainChoice === 'createGroceryList') {
    chooseDayToStart.innerHTML = enterNewRecipe.innerHTML;
    enterNewRecipe.parentNode.replaceChild(chooseDayToStart, enterNewRecipe);
  } else {
    alert('main choice not equal');
  }
}

function replaceGroceryListButton() {
  chooseDaysToPlan.innerHTML = createGroceryList.innerHTML;
  createGroceryList.parentNode.replaceChild(chooseDaysToPlan, createGroceryList);
}

enterNewRecipe.onclick = function() {
  var mainChoice = 'enterNewRecipe';
  localStorage.setItem('mainChoice', mainChoice);
  replaceNewRecipeButton(mainChoice);
}
  //enter ingredient names in text box, return recipe info to add_new_recipe()
function returnDayToPython(chooseDayToStart) {

}
/*
run read_recipe_storage() and enter_new_recipe() from python files, maybe make
text box that opens when enterNewRecipe() is called that allows user to enter
ingredient info?
*/

createGroceryList.onclick = function createGroceryList() {
  var mainChoice = 'createGroceryList';
  localStorage.setItem('mainChoice', mainChoice);
  replaceNewRecipeButton(mainChoice);
  replaceGroceryListButton();
}

//post button input to python script, need to rewrite python file to work with
//this
$.ajax({
  type: 'POST',
  url: '~/FoodListCreation.py',
  data: { param: chooseDayToStart}
})
// }).done(function( o ) {
//   // do something
// })

/*
run read_recipe_storage(),recipe_selection(), create_grocery_list(), and
output_grocery_list() when createGroceryList() is called
*/
