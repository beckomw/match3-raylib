
const r = require('raylib')

// ============================================
// CONFIGURATION
// ============================================
const CONFIG = {
    WINDOW_WIDTH: 1280,
    WINDOW_HEIGHT: 720,
    WINDOW_TITLE: "Operation Floppy Disk - Phase 1: Platform Test",
    TARGET_FPS: 60
};

// ============================================
// PLATFORM DEFINITION
// ============================================
const PLATFORM = {
    width: 500.0,
    length: 500.0,
    height: 0.2,
    position: { x: 0, y: -0.1, z: 0 },
    color: { r: 45, g: 45, b: 50, a: 255 },
    wallHeight: 4.0,
    wallThickness: 0.3,
    wallColor: { r: 35, g: 35, b: 40, a: 255 }
};

// ============================================
// PLAYER PLACEHOLDER (CUBE)
// ============================================
const PLAYER = {
    position: { x: 0, y: 0.9, z: 0 },
    size: { x: 0.6, y: 1.8, z: 0.6 },
    speed: 5.0,
    rotationSpeed: 3.0,
    rotationY: 0,
    color: { r: 60, g: 80, b: 120, a: 255 },
    wireColor: { r: 100, g: 140, b: 200, a: 255 }
};

// ============================================
// CAMERA SETUP (THIRD-PERSON OVER-SHOULDER)
// ============================================
const CAMERA_CONFIG = {
    offsetBack: 5.0,
    offsetUp: 3.0,
    offsetRight: 1.5,
    smoothing: 8.0
};

let camera = {
    position: { x: 1.5, y: 3.9, z: 5.0 },
    target: { x: 0, y: 0.9, z: 0 },
    up: { x: 0, y: 1, z: 0 },
    fovy: 60.0,
    projection: r.CAMERA_PERSPECTIVE
};

// ============================================
// SPAWN AREA (BURN MARKS)
// ============================================
const SPAWN = {
    position: { x: 0, y: 0.01, z: 0 },
    burnMarks: [
        { x: -1.0, z: -1.0, size: 0.8 },
        { x: 1.2, z: -0.8, size: 0.6 },
        { x: -0.5, z: 1.0, size: 0.7 },
        { x: 0.8, z: 1.2, size: 0.5 },
        { x: -1.2, z: 0.3, size: 0.6 },
        { x: 0.0, z: 0.0, size: 1.2 }
    ],
    color: { r: 25, g: 20, b: 20, a: 255 }
};

// ============================================
// INITIALIZATION
// ============================================
function init() {
    r.InitWindow(CONFIG.WINDOW_WIDTH, CONFIG.WINDOW_HEIGHT, CONFIG.WINDOW_TITLE);
    r.SetTargetFPS(CONFIG.TARGET_FPS);
    r.DisableCursor();
}

// ============================================
// INPUT & UPDATE
// ============================================
function updatePlayer(deltaTime) {
    // Rotation with arrow keys or Q/E
    if (r.IsKeyDown(r.KEY_LEFT) || r.IsKeyDown(r.KEY_Q)) {
        PLAYER.rotationY += PLAYER.rotationSpeed * deltaTime;
    }
    if (r.IsKeyDown(r.KEY_RIGHT) || r.IsKeyDown(r.KEY_E)) {
        PLAYER.rotationY -= PLAYER.rotationSpeed * deltaTime;
    }
    
    // Calculate forward and right vectors based on rotation
    const forward = {
        x: Math.sin(PLAYER.rotationY),
        z: Math.cos(PLAYER.rotationY)
    };
    const right = {
        x: Math.cos(PLAYER.rotationY),
        z: -Math.sin(PLAYER.rotationY)
    };
    
    // Movement with WASD
    let moveX = 0;
    let moveZ = 0;
    
    if (r.IsKeyDown(r.KEY_W) || r.IsKeyDown(r.KEY_UP)) {
        moveX -= forward.x;
        moveZ -= forward.z;
    }
    if (r.IsKeyDown(r.KEY_S) || r.IsKeyDown(r.KEY_DOWN)) {
        moveX += forward.x;
        moveZ += forward.z;
    }
    if (r.IsKeyDown(r.KEY_A)) {
        moveX -= right.x;
        moveZ -= right.z;
    }
    if (r.IsKeyDown(r.KEY_D)) {
        moveX += right.x;
        moveZ += right.z;
    }
    
    // Normalize diagonal movement
    const length = Math.sqrt(moveX * moveX + moveZ * moveZ);
    if (length > 0) {
        moveX /= length;
        moveZ /= length;
    }
    
    // Apply movement
    const newX = PLAYER.position.x + moveX * PLAYER.speed * deltaTime;
    const newZ = PLAYER.position.z + moveZ * PLAYER.speed * deltaTime;
    
    // Boundary collision (keep inside platform)
    const halfWidth = PLATFORM.width / 2 - PLAYER.size.x / 2 - PLATFORM.wallThickness;
    const halfLength = PLATFORM.length / 2 - PLAYER.size.z / 2 - PLATFORM.wallThickness;
    
    PLAYER.position.x = Math.max(-halfWidth, Math.min(halfWidth, newX));
    PLAYER.position.z = Math.max(-halfLength, Math.min(halfLength, newZ));
}

function updateCamera(deltaTime) {
    // Calculate desired camera position (behind and above player)
    const targetCamPos = {
        x: PLAYER.position.x + Math.sin(PLAYER.rotationY) * CAMERA_CONFIG.offsetBack + 
           Math.cos(PLAYER.rotationY) * CAMERA_CONFIG.offsetRight,
        y: PLAYER.position.y + CAMERA_CONFIG.offsetUp,
        z: PLAYER.position.z + Math.cos(PLAYER.rotationY) * CAMERA_CONFIG.offsetBack - 
           Math.sin(PLAYER.rotationY) * CAMERA_CONFIG.offsetRight
    };
    
    // Smooth camera follow
    const smooth = CAMERA_CONFIG.smoothing * deltaTime;
    camera.position.x += (targetCamPos.x - camera.position.x) * smooth;
    camera.position.y += (targetCamPos.y - camera.position.y) * smooth;
    camera.position.z += (targetCamPos.z - camera.position.z) * smooth;
    
    // Camera always looks at player (slightly above center)
    camera.target.x = PLAYER.position.x;
    camera.target.y = PLAYER.position.y + 0.5;
    camera.target.z = PLAYER.position.z;
}

function update() {
    const deltaTime = r.GetFrameTime();
    
    // Toggle cursor lock with ESC
    if (r.IsKeyPressed(r.KEY_ESCAPE)) {
        if (r.IsCursorHidden()) {
            r.EnableCursor();
        } else {
            r.DisableCursor();
        }
    }
    
    updatePlayer(deltaTime);
    updateCamera(deltaTime);
}

// ============================================
// RENDERING
// ============================================
function drawPlatform() {
    // Main floor
    r.DrawCube(
        PLATFORM.position,
        PLATFORM.width,
        PLATFORM.height,
        PLATFORM.length,
        PLATFORM.color
    );
    
    // Floor grid lines for visual reference
    r.DrawGrid(30, 1.0);
    
    // Perimeter walls
    const halfW = PLATFORM.width / 2;
    const halfL = PLATFORM.length / 2;
    const wallY = PLATFORM.wallHeight / 2;
    
    // Back wall (negative Z)
    r.DrawCube(
        { x: 0, y: wallY, z: -halfL },
        PLATFORM.width,
        PLATFORM.wallHeight,
        PLATFORM.wallThickness,
        PLATFORM.wallColor
    );
    
    // Front wall (positive Z)
    r.DrawCube(
        { x: 0, y: wallY, z: halfL },
        PLATFORM.width,
        PLATFORM.wallHeight,
        PLATFORM.wallThickness,
        PLATFORM.wallColor
    );
    
    // Left wall (negative X)
    r.DrawCube(
        { x: -halfW, y: wallY, z: 0 },
        PLATFORM.wallThickness,
        PLATFORM.wallHeight,
        PLATFORM.length,
        PLATFORM.wallColor
    );
    
    // Right wall (positive X)
    r.DrawCube(
        { x: halfW, y: wallY, z: 0 },
        PLATFORM.wallThickness,
        PLATFORM.wallHeight,
        PLATFORM.length,
        PLATFORM.wallColor
    );
}

function drawBurnMarks() {
    for (const mark of SPAWN.burnMarks) {
        r.DrawCylinder(
            { 
                x: SPAWN.position.x + mark.x, 
                y: SPAWN.position.y, 
                z: SPAWN.position.z + mark.z 
            },
            mark.size * 0.8,
            mark.size,
            0.02,
            16,
            SPAWN.color
        );
    }
}

function drawPlayer() {
    const cubeCenter = {
        x: PLAYER.position.x,
        y: PLAYER.position.y,
        z: PLAYER.position.z
    };
    
    // Draw solid cube
    r.DrawCube(
        cubeCenter,
        PLAYER.size.x,
        PLAYER.size.y,
        PLAYER.size.z,
        PLAYER.color
    );
    
    // Draw wireframe for visibility
    r.DrawCubeWires(
        cubeCenter,
        PLAYER.size.x,
        PLAYER.size.y,
        PLAYER.size.z,
        PLAYER.wireColor
    );
    
    // Draw facing direction indicator (small cube in front)
    const indicatorDistance = 0.5;
    const indicatorPos = {
        x: PLAYER.position.x - Math.sin(PLAYER.rotationY) * indicatorDistance,
        y: PLAYER.position.y + 0.5,
        z: PLAYER.position.z - Math.cos(PLAYER.rotationY) * indicatorDistance
    };
    r.DrawCube(indicatorPos, 0.15, 0.15, 0.15, { r: 200, g: 200, b: 100, a: 255 });
}

function drawDebugInfo() {
    r.DrawRectangle(10, 10, 280, 180, { r: 0, g: 0, b: 0, a: 200 });
    
    r.DrawText("PHASE 1: 3D PLATFORM TEST", 20, 20, 14, r.GREEN);
    r.DrawText("─────────────────────────", 20, 38, 14, r.DARKGREEN);
    
    r.DrawText(`Player Position:`, 20, 55, 12, r.LIGHTGRAY);
    r.DrawText(`  X: ${PLAYER.position.x.toFixed(2)}`, 20, 70, 12, r.WHITE);
    r.DrawText(`  Y: ${PLAYER.position.y.toFixed(2)}`, 20, 85, 12, r.WHITE);
    r.DrawText(`  Z: ${PLAYER.position.z.toFixed(2)}`, 20, 100, 12, r.WHITE);
    
    r.DrawText(`Rotation: ${(PLAYER.rotationY * 180 / Math.PI).toFixed(1)}°`, 20, 120, 12, r.WHITE);
    
    r.DrawText("─────────────────────────", 20, 138, 14, r.DARKGREEN);
    r.DrawText("WASD: Move  |  Q/E: Rotate", 20, 155, 10, r.GRAY);
    r.DrawText("ESC: Toggle cursor lock", 20, 170, 10, r.GRAY);
    
    r.DrawFPS(CONFIG.WINDOW_WIDTH - 90, 10);
}

function draw() {
    r.BeginDrawing();
    r.ClearBackground({ r: 15, g: 15, b: 20, a: 255 });
    
    r.BeginMode3D(camera);
    
    drawPlatform();
    drawBurnMarks();
    drawPlayer();
    
    r.EndMode3D();
    
    drawDebugInfo();
    
    r.EndDrawing();
}

// ============================================
// MAIN GAME LOOP
// ============================================
function main() {
    init();
    
    while (!r.WindowShouldClose()) {
        update();
        draw();
    }
    
    r.CloseWindow();
}

// Run the game
main();

