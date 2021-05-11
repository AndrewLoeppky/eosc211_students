---
jupyter:
  jupytext:
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.2'
      jupytext_version: 1.5.1-dev
---

<!-- #region -->

# Slide 0
```

Week 11:  Spacecraft flybys of Planets
Concept: Use of planetary flybys to modify spacecraft trajectories
A color composite image of Earth 9/22/17 taken by the MapCam camera on NASA’s OSIRIS-REx spacecraft. This image was taken just hours after the spacecraft completed its Earth Gravity Assist at a range of approximately 106,000 miles (170,000 kilometers).
Visible in this image are the Pacific Ocean and several familiar landmasses, including Australia in the lower left, and Baja California and the southwestern United States in the upper right.
The dark vertical streaks at the top of the image are caused by short exposure times (less than three milliseconds). Short exposure times are required for imaging an object as bright as Earth, but are not anticipated for an object as dark as the asteroid Bennu, which the camera was designed to image.

```





<img src="media11\week11_numericalint-slide_0-000.png">

<!-- #endregion -->

<!-- #region -->

# Slide 1
```

Week 11:  Assignment 2 Background
Concept:
Use of planetary flybys to modify spacecraft trajectories
Physics needed:   Newton’s laws (gravitation & motion), resolving vectors
MATLAB:  use skills from this class! Learn basics of numerical integration

```





<img src="media11\week11_numericalint-slide_1-001.png">


<img src="media11\week11_numericalint-slide_1-002.png">

<!-- #endregion -->


# Slide 2
```

Real Planetary Flybys
Animations - MESSENGER Mission Website:   THIS WAS NOT WORKING FOR ME AS OF THIS WEEK…..
“Gravity Assist Simulator” (copy and paste the following link)
http://btc.montana.edu/messenger/Interactives/ANIMATIONS/grav_assist/gravity_assist.html
What happens to the spacecraft speed and direction depends on
How close it flies to the planet
The relative motion of the s/c and planet
See also:
http://www.planetary.org/blogs/guest-blogs/2013/20130926-gravity-assist.html

```


<!-- #region -->

# Slide 3
```

From the planet’s perspective:
planet is stationary, spacecraft moves relative to the planet
e.g. our assignment!!

```





<img src="media11\week11_numericalint-slide_3-003.png">

<!-- #endregion -->

<!-- #region -->

# Slide 4
```

Boosting a spacecraft’s speed:
e.g. getting to the outer solar system using Jupiter
e.g. New Horizons, Voyager missions,….

```





<img src="media11\week11_numericalint-slide_4-004.png">

<!-- #endregion -->

<!-- #region -->

# Slide 5
```

Slowing a spacecraft’s speed:
e.g. getting into orbit around a planet in the inner solar system
e.g. MESSENGER mission to Mercury

```





<img src="media11\week11_numericalint-slide_5-005.png">

<!-- #endregion -->

<!-- #region -->

# Slide 6
```

Assignment 2:
Mimics the flybys of Mercury by the MESSENGER spacecraft
Spacecraft starts out distant from Mercury, with speed 7 km/s
Flies to within ~200 km of surface in our assignment (was to within 201 km of surface in actual flybys).
Aside:  7 km/s = 3600*7 km/hr, so over 25,000 km/hr!

```





<img src="media11\week11_numericalint-slide_6-006.png">

<!-- #endregion -->

<!-- #region -->

# Slide 7
```

The assignment:
Given
the initial (t=0) spacecraft velocity vector
the initial (t=0) spacecraft position vector
a time increment at which to calculate positions
Calculate the entire spacecraft trajectory until a time t= tfinal

```





<img src="media11\week11_numericalint-slide_7-007.png">

<!-- #endregion -->

<!-- #region -->

# Slide 8
```

How to do this…..
Spacecraft is moving with initial velocity, v in the direction shown.  It is at some known position relative to the center of the planet.
In the absence of the planet assume there are no other forces on the spacecraft (e.g., no rocket burns, no drag etc).
v

```





<img src="media11\week11_numericalint-slide_8-008.png">


<img src="media11\week11_numericalint-slide_8-009.png">

<!-- #endregion -->

<!-- #region -->

# Slide 9
```

How to do this…..
Spacecraft is moving with initial velocity, v in the direction shown.  It is at some known position relative to the center of the planet.
The sketches below describe the instantaneous directions of force, acceleration and velocity experienced by the spacecraft:
v
F, a
planet
v
F, a
planet
A
B
A) at time t= 0
v
B) at time t= t later
Notice that because the acceleration had components both parallel and perpendicular to the spacecraft’s initial velocity both the magnitude and direction of velocity are changed

```





<img src="media11\week11_numericalint-slide_9-010.png">


<img src="media11\week11_numericalint-slide_9-011.png">

<!-- #endregion -->


# Slide 10
```

How to calculate the acceleration of the spacecraft
Direction of F, a (due to the planet) is shown in blue.
F = G Mp m / s2				Newton’s Law of Gravitation
Mp=mass planet, m = mass spacecraft, s is distance between them
a = acceleration = F / m = G Mp / s2		 Newton’s 2nd Law of Motion
acceleration, a = F / m
a = (ax, ay)
planet
Use a coordinate system with origin at the planet’s center with x and y directions shown.
The acceleration can be resolved into two perpendicular components, ax and ay.
b
original direction of s/c motion
ax = a sin()
ay = a cos()
sin(  = -sx/s
cos( = -sy/s
s = (sx, sy)

```




# Slide 11
```

Calculating the spacecraft trajectory
acceleration in the direction of the planet, a = G Mp / s2
acceleration, a = F / m
a = (ax, ay)
planet
resolve into two perpendicular components, ax and ay
After a time Dt
ax and ay have changed the x- and y- components of the velocity
=> resulting in a new speed and new direction of motion
they also change the x- and y- components of position
=> resulting in a new spacecraft position
b
original direction of s/c motion
ax = a sin()
ay = a cos()
sin(  = -sx/s
cos( = -sy/s
s = (sx, sy)
WORKSHEET

```


<!-- #region -->

# Slide 12
```

Part 5 Results

```





<img src="media11\week11_numericalint-slide_12-012.png">


<img src="media11\week11_numericalint-slide_12-013.png">

<!-- #endregion -->

<!-- #region -->

# Slide 13
```

And … unrelated to flybys but also planetary…
InSight Landing – Nov 26, 2018 = MONDAY Week 13, Noon PST.
https://mars.nasa.gov/insight/timeline/landing/watch-online/
Stop by to ‘watch’ in the Pacific Museum of Earth, EOS Main Lobby
11:00 am – 1:00 pm, 11/26/2018

```





<img src="media11\week11_numericalint-slide_13-014.png">


<img src="media11\week11_numericalint-slide_13-015.png">


<img src="media11\week11_numericalint-slide_13-016.png">

<!-- #endregion -->
