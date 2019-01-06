# VirtualCube
VirtualCube is a Python based solution which provides a user with a programmatic representation of the Rubik's Cube.

<h3>Using VirtualCube</h3>
Clone the repository, and import the Cube.py file into your Python script.

<h3>Usage Example</h3>

```python
myCube = Cube()
myCube.outputCube()
myCube.rotateEquatorial(Color.BLUE)
myCube.rotateAxial(Color.WHITE)
print(myCube.isSolved())
myCube.outputCube()
```
