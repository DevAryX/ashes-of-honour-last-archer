# Ashes of Honour: Last Archer

## Overview
**Ashes of Honour: Last Archer** is a 2D arcade-style survival shooter developed in **Python using Pygame**. The game was created as part of my **NPA Level 6 Games Design** course work and represents the final implementation of my *Assessment 2b* proposal.

The project focuses on fast-paced, skill-based gameplay, where the player must survive against infinite waves of undead enemies while achieving the highest possible score.

---

## Project Context (Assessment Information)
- **Course:** NPA Level 6 Games Design
- **Assessment:** Assessment 2b – Solo Game Development Project
- **Purpose:** Design, develop, and evaluate a complete playable game based on an original proposal
- **Engine / Technology:** Python + Pygame (2D)
- **Platform:** Windows PC (Desktop)

This game is a *scaled-down playable moment* set in the wider fictional world of **Ashes of Honour**, designed to demonstrate core game design principles, programming skills, and gameplay polish within a limited scope.

---

## Genre & Theme
- **Genre:**
  - 2D Action Arcade Shooter
  - Survival / Wave Defence
- **Theme:**
  - Medieval dark fantasy
  - Gritty, high-tension dungeon survival

The visual tone is dark and atmospheric, featuring torch-lit stone corridors, undead enemies, and audio-visual feedback designed to enhance immersion.

---

## Narrative / Objective
**Premise:**  
During the collapse of the realm of *Eryndor*, cursed undead remnants rise within the forgotten dungeons beneath the capital. You play as **The Last Archer**, a loyal scout of the Fallen One, trapped alone in a narrow corridor.

Your task is simple but unforgiving:
> **Hold the choke-point and survive for as long as possible.**

Reinforcements will never arrive.

### Core Objective
- Survive infinite waves of skeleton enemies
- Achieve the highest possible score

### Scoring System
- **+1 point** — Normal kill
- **+2 points** — Headshot (top third of enemy hitbox)

---

## Controls
**Keyboard + Mouse**
- **WASD** — Move player
- **Mouse Movement** — Aim
- **Left Mouse Button** — Shoot arrow

### Automatic Systems
- **Fire Arrow Mode** activates automatically every 20 seconds (lasts 5 seconds)
- **Slow-Motion Effect** triggers automatically when the player is hit
- No menus — the game ends immediately upon death

---

## Gameplay & Mechanics
### Core Mechanics
- **Manual Shooting & Aiming** — precision-based combat
- **Headshot System** — rewards accuracy with bonus points and visual feedback
- **Infinite Wave Spawning** — enemies increase in frequency over time
- **Slow-Motion Death Vision** — one final moment before defeat

### Feedback & Effects
- Screen shake on headshots
- Floating "HEADSHOT!" text
- Dynamic audio (shooting, headshots, background music)
- Screen darkening during slow-motion

There is **no win condition** — the experience is designed as a score-chasing survival challenge.

---

## Characters
### Player — The Last Archer
- Silent scout trained by the Fallen One
- Fast movement and simple two-frame animation
- High-risk, high-skill playstyle
- No armour — one mistake can end the run

### Enemies — Skeletons
- Undead soldiers from a fallen faction
- Approach from the right side of the screen
- Randomised movement speed
- Infinite waves with increasing difficulty

---

## Level / Environment Design
- Single long dungeon corridor
- Static background scaled to screen resolution
- No obstacles — pure reaction-based survival
- All pressure comes from one direction to reinforce tension

This minimal environment keeps the focus on clarity, performance, and moment-to-moment gameplay.

---

## User Interface
- Minimal HUD
- Score counter (top-left)
- Floating combat text
- Visual overlays for slow-motion

The UI is intentionally simple to maintain an arcade-style experience.

---

## Requirements
- Python **3.10+**
- Pygame

Install dependencies using:
```bash
pip install -r requirements.txt
```

---

## How to Run
1. Clone the repository
2. Install dependencies from `requirements.txt`
3. Run the main game file:
```bash
python main.py
```

---

## Comparison & Evaluation
As part of the course, this game was reviewed and compared against **Vampire Survivors**, a commercial title in the same survival genre.

### Overall Strengths
- Responsive, skill-based gameplay
- Clear visual and audio feedback
- Strong core loop despite limited scope

### Areas for Improvement
- Additional enemy types
- Expanded environments
- Deeper narrative elements

Despite its simplicity, **Ashes of Honour: Last Archer** succeeds as a polished, replayable arcade survival experience suitable for a solo Level 6 project.

---

## Future Improvements
- Multiple enemy variations
- Upgrade and progression systems
- Additional levels or environments
- Leaderboard / score saving

---

## Credits
Developed by **Arham (Ary)**  
NPA Level 6 Games Design — School Project

All assets and audio are used for educational purposes only.

