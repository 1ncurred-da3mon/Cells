# Cells

>Inspired by SenseHAT Emulator on the Raspberry Pi. Using a 6x5 Grid (implemented with Turtle), you can create little animations with the "Cells" by changing the color of the Cells. This is more of a project for fun, not entirely optimized for performance.

I was looking for a SenseHAT Emulator for Windows, however, I could not find anything (at least on the surface of the internet), so I took matters into my own hands and created "Cells".

Using my not-so-efficient scripting language "Cell Script", you can animate the cells with simple to understand code. 

## Example Code:
```
// Create a function called "draw_c
func draw_c
	// fill the following dots on the grid with the color cyan
	set a2 a3 a4 b1 c1 d1 e2 e3 e4 cyan
// end the function
end

// call draw_c
draw_c
```
## Result:
<p><img src="https://i.imgur.com/Cb8nCAi.png"/></p>

My program is not perfect right now with random crashes, but I'm still working on it.

## Requirements
- Python (v3.8)
- Turtle
