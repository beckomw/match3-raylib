#include "raylib.h" 
#include "raymath.h" 


void GameStartup() {}
void GameUpdate() {}
void GameRender() {}
void GameShutdown() {}

const int screenWidth = 800; 
const int screenHeight = 600; 


int main() 
{
  InitWindow(screenWidth, screenHeight, "Raylib 2D RPG DEMO"); 
  SetTargetFPS(60); 
  
  GameStartup(); 


  while(!WindowShouldClose()) {


      GameUpdate(); 
      
      BeginDrawing(); 
      ClearBackground(GRAY); 

      GameRender(); 

      EndDrawing(); 



  }
    



      GameShutdown(); 

      CloseWindow(); 
      return 0; 
      

  }
