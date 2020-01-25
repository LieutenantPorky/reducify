import 'package:flutter/material.dart';
import 'package:flutter/widgets.dart';
import 'recipeitem.dart';
import 'dart:convert';
import 'webservice.dart';


class RecipeListState extends State<RecipeList> {

  List<Recipe> _recipes = List<Recipe>();

  @override
  void initState() {
    super.initState();
    _populateRecipes();
  }

  void _populateRecipes() {

    Webservice().load(Recipe.all).then((recipes) => {
  setState(() => {
    _recipes = recipes
  })
});

    // Webservice().load(Recipe.all).then((recipes) => {
      // setState(() => {
      //   _recipes = [
      //     Recipe(name:"testItem", date:"never",number:5),
      //     Recipe(name:"Cookies", date:"never",number:200),
      //   ],
      //   token="putTokenHere"
      // });
    // });


  }

  Card _buildItemsForListView(BuildContext context, int index) {
     return Card(
       child: ListTile(
         title: Center(
           child: Text(_recipes[index].name, style: TextStyle(fontSize: 20)),
         ),
         subtitle: Center(
           // child: Text("quantity: ${_recipes[index].number.toString()}", style: TextStyle(fontSize: 18))
         ),
       )
     );
 }


  @override
  Widget build(BuildContext context) {
    return ListView.builder(
      itemCount: _recipes.length,
      itemBuilder: _buildItemsForListView,
    );
  }
}

class RecipeList extends StatefulWidget {

  @override
  createState() => RecipeListState();
}
