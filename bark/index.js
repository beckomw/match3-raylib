// Node-Raylib
const r = require('raylib')

const screenWidth = 1280
const screenHeight = 720

r.InitWindow(screenWidth, screenHeight, "Node-Raylib example - 3D Platform")

// Define the camera
const camera = new r.Camera3D(
  new r.Vector3(5.0, 1.0, 5.0), // Camera position
  new r.Vector3(0.0, 3.0, 0.0),    // Camera looking at point
  new r.Vector3(0.2, 0.1, 0.1),    // Camera up vector (rotation towards target)
  45.0,                           // Camera field-of-view Y
  r.CAMERA_PERSPECTIVE             // Camera mode
);

// Create a platform
const platformMesh = r.GenMeshCube(100.0, 1.0, 100.0)
const platformModel = r.LoadModelFromMesh(platformMesh)

// Create a cube to move around
const cubePosition = new r.Vector3(0.0, 1.0, 0.0)
const cubeSize = new r.Vector3(1.0, 1.0, 1.0)

r.SetTargetFPS(60)

while (!r.WindowShouldClose()) {
  // Update
  r.UpdateCamera(camera, r.CAMERA_ORBITAL)

  if (r.IsKeyDown(r.KEY_RIGHT)) cubePosition.x += 0.1
  if (r.IsKeyDown(r.KEY_LEFT)) cubePosition.x -= 0.1
  if (r.IsKeyDown(r.KEY_DOWN)) cubePosition.z += 0.1
  if (r.IsKeyDown(r.KEY_UP)) cubePosition.z -= 0.1


  // Draw
  r.BeginDrawing()
  r.ClearBackground(r.RAYWHITE)

  r.BeginMode3D(camera)

  r.DrawModel(platformModel, new r.Vector3(0, 0, 0), 1.0, r.BLACK)
  r.DrawCubeV(cubePosition, cubeSize, r.RED)
  r.DrawGrid(20, 1.0)

  r.EndMode3D()

  r.DrawText(" - 32 44 Project Embark", 10, 10, 20, r.DARKGRAY)
 


  r.EndDrawing()
}

r.CloseWindow()
