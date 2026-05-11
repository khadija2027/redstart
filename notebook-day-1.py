import marimo

__generated_with = "0.20.4"
app = marimo.App()


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    # Redstart: A Lightweight Reusable Booster
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.image(src="public/images/redstart.png")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Project Redstart is an attempt to design the control systems of a reusable booster during landing.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    In principle, it is similar to SpaceX's Falcon Heavy Booster.

    >The Falcon Heavy booster is the first stage of SpaceX's powerful Falcon Heavy rocket, which consists of three modified Falcon 9 boosters strapped together. These boosters provide the massive thrust needed to lift heavy payloads—like satellites or spacecraft—into orbit. After launch, the two side boosters separate and land back on Earth for reuse, while the center booster either lands on a droneship or is discarded in high-energy missions.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.center(
        mo.Html("""
    <iframe width="560" height="315" src="https://www.youtube.com/embed/RYUr-5PYA7s?si=EXPnjNVnqmJSsIjc" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>""")
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Dependencies
    """)
    return


@app.cell
def _():
    import scipy
    import scipy.integrate as sci

    import matplotlib as mpl
    import matplotlib.pyplot as plt

    import numpy as np
    import numpy.linalg as la

    return np, plt, sci


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## The Model

    The Redstart booster in model as a rigid tube of length $\ell$ and negligible diameter whose mass $M$ is uniformly spread along its length. It may be located in 2D space by the coordinates $(x, y)$ of its center of mass and the angle $\theta$ it makes with respect to the vertical (with the convention that $\theta > 0$ for a left tilt, i.e. the angle is measured counterclockwise)

    This booster has an orientable reactor at its base ; the force that it generates is of amplitude $f \geq 0$ and the angle of the force with respect to the booster axis is $\phi$ (with a counterclockwise convention).

    We assume that the booster is subject to gravity, the reactor force and that the friction of the air is negligible.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.center(mo.image(src="public/images/geometry.svg"))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Constants

    For the sake of simplicity (this is merely a toy model!) in the sequel we assume that:

    - the total length $\ell$ of the booster is 2 meters,
    - its mass $M$ is 1 kg,
    - the gravity constant $g$ is 1 m/s^2.

    This set of values is completely unrealistic, but very simple! It will simplify our computations and will not fundamentally impact the structure of the booster dynamics.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Getting Started
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Constants

    Define the Python constants `g`, `M` and `l` that correspond to the gravity constant, the mass and half-length of the booster.
    """)
    return


@app.cell
def _():
    # Constants
    g = 1.0      # gravitational acceleration (m/s^2)
    M = 1.0      # mass of the booster (kg)
    l = 1.0      # half-length of the booster (m), total length = 2*l = 2 m
    return M, g, l


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Forces

    Compute the cartesian coordinates $f_x$ and $f_y$ of the force applied to the booster by the reactor, functions of $f$, $\theta$ and $\phi$.
    """)
    return


@app.cell
def _(np):
    def F_x(f, theta, phi):
        fx = -f * np.sin(theta + phi)
        return fx

    def F_y(f, theta, phi):
        fy =  f * np.cos(theta + phi)
        return fy    
    

    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Center of Mass

    Give the ordinary differential equation that governs the evolution of the position $(x, y)$ of the center of mass of the booster.
    """)
    return


@app.cell
def _(M, g):
    def Center_mass(fx, fy):
        xddot = fx / M
        yddot = fy / M - g

        return xddot, yddot

    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Moment of inertia

    Compute the [moment of inertia](https://en.wikipedia.org/wiki/Moment_of_inertia) $J$ of the booster and define the corresponding Python variable `J`.
    """)
    return


@app.cell
def _(M, l):
    J = (1/3) * M * l**2
    return (J,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Tilt

    Give the ordinary differential equation that governs the evolution of the tilt angle $\theta$.
    """)
    return


@app.cell
def _(J, l, np):
    def Tilt(f, theta, phi):
        """
        Returns theta_ddot.
        """
        # Torque about the center of mass:
        # tau = -l * f * sin(phi)
        theta_ddot = -l * f * np.sin(phi) / J
        return theta_ddot

    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Vector Field

    Denote

    - $v_x =\dot{x}$, $v_y = \dot{y}$ the components of the booster center of mass velocity,
    - $\omega = \dot{\theta}$ the angular velocity of the booster.


    What is is dimension $n$ of the state space?
    What is the state $s \in \R^n$ of the booster dynamics?
    Provide the definition of the function $F : \mathbb{R}^{n + 2} \to \mathbb{R}^n$ such that the system evolves
    according to

    $$
    \dot{s} = F(s, f, \phi).
    $$
    """)
    return


@app.cell
def _(J, M, g, l, np):
    def F(t, s, f, phi):
        x, vx, y, vy, theta, omega = s
    
        # Compute forces
        fx = -f * np.sin(theta + phi)
        fy = f * np.cos(theta + phi)
    
        # Linear accelerations
        xddot = fx / M
        yddot = fy / M - g
    
        # Rotational acceleration
        theta_ddot = -l * f * np.sin(phi) / J
    
        return np.array([
            vx,            # x_dot
            xddot,         # vx_dot
            vy,            # y_dot
            yddot,         # vy_dot
            omega,         # theta_dot
            theta_ddot     # omega_dot
        ])

    return (F,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Simulation

    Define a function `redstart_solve` that, given the input parameters:

    - `t_span`: a pair of initial time `t_0` and final time `t_f`,
    - `y0`: the value of `[x, vx, y, vy, theta, omega]` at `t_0`,
    - `f_phi`: a function that given the current time `t` and current state value `y`
         returns the values of the inputs `f` and `phi` in an array.

    returns:

    - `sol`: a function that given a time `t` returns the value of `[x, vx, y, vy, theta, omega]` at time `t` (and that also accepts 1d-arrays of times for multiple state evaluations).

    A typical usage would be:

    ```python
    def free_fall_example():
        t_span = [0.0, 5.0]
        y0 = [0.0, 0.0, 10.0, 0.0, 0.0, 0.0] # [x, vx, y, vy, theta, omega]
        def f_phi(t, y):
            return np.array([0.0, 0.0]) # [f, phi]
        sol = redstart_solve(t_span, y0, f_phi)
        t = np.linspace(t_span[0], t_span[1], 1000)
        y_t = sol(t)[2]
        plt.plot(t, y_t, label=r"$y(t)$ (height in meters)")
        plt.plot(t, l * np.ones_like(t), color="grey", ls="--", label=r"$y=\ell$")
        plt.title("Free Fall")
        plt.xlabel("time $t$")
        plt.grid(True)
        plt.legend()
        return plt.gcf()
    free_fall_example()
    ```
    """)
    return


@app.cell
def _(F, sci):
    def redstart_solve(t_span, y0, f_phi):
        """
        Parameters
        ----------
        t_span : [t0, tf]
        y0 : initial state [x, vx, y, vy, theta, omega]
        f_phi : function (t, y) -> [f, phi]

        Returns
        -------
        sol : callable
            sol(t) returns the state at time t.
        """
        def rhs(t, y):
            f, phi = f_phi(t, y)
            return F(t, y, f, phi)

        result = sci.solve_ivp(
            rhs,
            t_span,
            y0,
            dense_output=True
        )

        return result.sol

    return (redstart_solve,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Freefall test


    In the `free_fall` example scenario. scenario, at what moment should the center of mass of the booster theoretically cross the
    height of $y = \ell$?

    Check your `redstart_solve` function in this scenario and produce a graph that allows us to check the above answer numerically/visually.
    """)
    return


@app.cell
def _(l, np, plt, redstart_solve):
    def free_fall_example():
        t_span = [0.0, 5.0]
        y0 = [0.0, 0.0, 10.0, 0.0, 0.0, 0.0]  # [x, vx, y, vy, theta, omega]
    
        def f_phi(t, y):
            return np.array([0.0, 0.0])  # [f, phi]
    
        sol = redstart_solve(t_span, y0, f_phi)
        t = np.linspace(t_span[0], t_span[1], 1000)
        y_t = sol(t)[2]  # y position
    
        # Find when y = l
        from scipy.optimize import fsolve
        t_cross = fsolve(lambda t: sol(t)[2] - l, 2.0)[0]
    
        print(f"Theoretical: y(t) = y0 + vy0*t - 0.5*g*t^2")
        print(f"Solving l = 10 - 0.5*1*t^2 => t = sqrt(2*(10-1)) = {np.sqrt(2*(10-1)):.3f} s")
        print(f"Numerical crossing time: {t_cross:.3f} s")
    
        plt.figure(figsize=(10, 6))
        plt.plot(t, y_t, label=r"$y(t)$ (height in meters)", linewidth=2)
        plt.plot(t, l * np.ones_like(t), color="grey", ls="--", linewidth=2, label=r"$y=\ell$ (1 m)")
        plt.axhline(y=0, color='brown', ls='-', linewidth=1, label="Ground")
        plt.title("Free Fall Trajectory", fontsize=14)
        plt.xlabel("time $t$ (s)", fontsize=12)
        plt.ylabel("height $y$ (m)", fontsize=12)
        plt.grid(True, alpha=0.3)
        plt.legend()
        return plt.gcf()

    free_fall_example()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Controlled Landing

    Assume that $x$, $\dot{x}$, $\theta$ and $\dot{\theta}$ are null at $t=0$ and that $y(0)= 10$ and $\dot{y}(0) = - 2$.

    Find a time-varying force $f(t)$ which, when applied in the booster axis ($\theta=0$), yields $y(5)=\ell / 2 = 1$ (the booster is at ground level) and $\dot{y}(5)=0$ (the booster is at rest).

    Simulate the corresponding scenario, display graphically the results and check that your solution works as expected.
    """)
    return


@app.cell
def _(M, g, l, np, plt, redstart_solve):
    def controlled_landing_example():
        t_span = [0.0, 5.0]
        y0 = [0.0, 0.0, 10.0, -2.0, 0.0, 0.0]  # [x, vx, y, vy, theta, omega]
    
        # Desired trajectory: y(t) = a*t^4 + b*t^3 + c*t^2 + d*t + e
        # with constraints: y(0)=10, y(5)=1, y'(0)=-2, y'(5)=0, y''(5)=0
        # Solving the system:
        # e = 10
        # d = -2
        # 625a + 125b + 25c + 5d + e = 1
        # 500a + 75b + 10c + d = 0
        # 300a + 30b + 2c = 0
    
        # Solve the linear system
        A = np.array([[625, 125, 25],
                      [500, 75, 10],
                      [300, 30, 2]])
        b_vec = np.array([1 - 5*(-2) - 10, 0 - (-2), 0])
        abc = np.linalg.solve(A, b_vec)
        a, b, c = abc
    
        def desired_acceleration(t):
            """Compute required acceleration for desired trajectory"""
            # y_ddot = 12*a*t^2 + 6*b*t + 2*c
            return 12*a*t**2 + 6*b*t + 2*c
    
        def f_phi(t, y):
            # y_ddot = f/M - g => f = M*(y_ddot + g)
            if t < 5.0:
                f = M * (desired_acceleration(t) + g)
                f = max(0, f)  # Force can't be negative
            else:
                f = M * g  # Hover after landing
            return np.array([f, 0.0])
    
        sol = redstart_solve(t_span, y0, f_phi)
        t = np.linspace(t_span[0], t_span[1], 1000)
        states = sol(t)
        y_t = states[2]
        vy_t = states[3]
    
        fig, axes = plt.subplots(2, 2, figsize=(12, 8))
    
        axes[0,0].plot(t, y_t, linewidth=2)
        axes[0,0].axhline(y=l/2, color='r', ls='--', label='Target height (1m)')
        axes[0,0].set_ylabel('Height y (m)')
        axes[0,0].set_title('Position')
        axes[0,0].grid(True, alpha=0.3)
        axes[0,0].legend()
    
        axes[0,1].plot(t, vy_t, linewidth=2, color='orange')
        axes[0,1].axhline(y=0, color='r', ls='--', label='Target velocity (0)')
        axes[0,1].set_ylabel('Velocity vy (m/s)')
        axes[0,1].set_title('Velocity')
        axes[0,1].grid(True, alpha=0.3)
        axes[0,1].legend()
    
        # Compute actual acceleration and force
        dt = t[1] - t[0]
        accel = np.gradient(vy_t, dt)
        force = M * (accel + g)
    
        axes[1,0].plot(t, force, linewidth=2, color='green')
        axes[1,0].axhline(y=M*g, color='b', ls='--', label='Hover force (Mg)')
        axes[1,0].set_ylabel('Force f (N)')
        axes[1,0].set_xlabel('Time t (s)')
        axes[1,0].set_title('Required Force')
        axes[1,0].grid(True, alpha=0.3)
        axes[1,0].legend()
    
        axes[1,1].plot(t, desired_acceleration(t), label='Desired', linewidth=2)
        axes[1,1].plot(t, accel, '--', label='Actual', linewidth=2)
        axes[1,1].set_ylabel('Acceleration (m/s²)')
        axes[1,1].set_xlabel('Time t (s)')
        axes[1,1].set_title('Acceleration Tracking')
        axes[1,1].grid(True, alpha=0.3)
        axes[1,1].legend()
    
        plt.tight_layout()
        return plt.gcf()

    controlled_landing_example()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Animations

    It's very handy to visualize the evolution of our booster "as a movie"!

    Have a look at the [animations tutorial] to understand the basics of animated SVG documents.

    [animations tutorial]: http://localhost:2718/?file=animations.py
    """)
    return


@app.cell
def _():
    from svg import svg, transform, animate_transform

    return (svg,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Environment

    Create a function `world` whose arguments are:

    - `view_box`: a view box in cartesian coordinates `[x_min, x_max, y_min, y_max]`,

    - `*objects`: (optional) list of extra svg elements (default : `[]`).

    and that returns a SVG string which

    - has the appropriate cartesian view box and frame ($y$-axis upwards),

    - depicts the sky and the ground,

    - depicts a 2 meter wide green ground target centered on $(0, 0)$,

    - displays the objects (if any) inserted on top of the world.

    Test your function with the following scenes:

    ```python
    mo.hstack(
        [
            # Display an empty world
            mo.Html(
                world([-3, 3, -2, 4])
            ),
            # Display a world with a black square on top of the landing pad
            mo.Html(
                world(
                    [-3, 3, -2, 4],
                    svg.rect(x=-1, y=0, width=2, height=2, fill="black"),
                )
            ),
            # Display a world with a red square in the top-left corner of the view box
            # and a blue square on the top-right corner of the view box.
            mo.Html(
                world(
                    [-3, 3, -2, 4],
                    svg.rect(x=-3, y=2, width=2, height=2, fill="red"),
                    svg.rect(x=1, y=2, width=2, height=2, fill="blue"),
                )
            )
        ],
        justify="space-around"
    )
    ```
    """)
    return


@app.cell
def _(mo, svg):
    def world(view_box, *objects):
        """
        Create an SVG world with sky, ground, and a landing pad.

        Parameters
        ----------
        view_box : [x_min, x_max, y_min, y_max]
            Cartesian coordinates (y-axis points upward).
        *objects :
            Optional SVG elements to overlay on the world.
        """
        x_min, x_max, y_min, y_max = view_box

        # Dimensions of the SVG viewBox
        width = x_max - x_min
        height = y_max - y_min

        # Background elements in Cartesian coordinates
        # Sky: from y = 0 to y = y_max
        sky = (
            f'<rect x="{x_min}" y="0" '
            f'width="{width}" height="{y_max}" '
            f'fill="#87CEEB"/>'
        )

        # Ground: from y = y_min to y = 0
        ground = (
            f'<rect x="{x_min}" y="{y_min}" '
            f'width="{width}" height="{0 - y_min}" '
            f'fill="#8B4513"/>'
        )

        # Grass strip at y = 0
        grass = (
            f'<rect x="{x_min}" y="0" '
            f'width="{width}" height="0.05" '
            f'fill="#228B22"/>'
        )

        # Landing pad
        landing_pad = """
        <rect x="-1" y="-0.05" width="2" height="0.05"
              fill="#00AA00"
              stroke="#006600"
              stroke-width="0.02"
              rx="0.02"/>
        """

        # Target marker
        target_marker = """
        <circle cx="0" cy="-0.025" r="0.15"
                fill="#FF0000"
                opacity="0.8"/>
        """

        # Crosshair
        crosshair_h = """
        <line x1="-0.1" y1="-0.025"
              x2="0.1"  y2="-0.025"
              stroke="#FFFFFF"
              stroke-width="0.02"/>
        """

        crosshair_v = """
        <line x1="0" y1="-0.125"
              x2="0" y2="0.075"
              stroke="#FFFFFF"
              stroke-width="0.02"/>
        """

        # Combine built-in elements
        elements = [
            sky,
            ground,
            grass,
            landing_pad,
            target_marker,
            crosshair_h,
            crosshair_v,
        ]

        # Add user-provided SVG objects
        for obj in objects:
            elements.append(str(obj))

        # Invert Y-axis so Cartesian coordinates behave naturally:
        # y increases upward and the sky appears at the top.
        group = f"""
        <g transform="translate(0,{y_min + y_max}) scale(1,-1)">
            {''.join(elements)}
        </g>
        """

        # Final SVG
        svg_string = f"""
        <svg viewBox="{x_min} {y_min} {width} {height}"
             width="100%"
             height="100%"
             preserveAspectRatio="xMidYMid meet"
             xmlns="http://www.w3.org/2000/svg">
            {group}
        </svg>
        """

        return svg_string


    # ---------------------------------------------------------------------
    # Example tests
    # ---------------------------------------------------------------------
    def test_world():
        # Test 1: Empty world
        world1 = world([-3, 3, -2, 4])

        # Test 2: Black square above landing pad
        world2 = world(
            [-3, 3, -2, 4],
            svg.rect(
                x=-1,
                y=0,
                width=2,
                height=2,
                fill="black",
                opacity=0.7,
            ),
        )

        # Test 3: Red square upper-left and blue square upper-right
        world3 = world(
            [-3, 3, -2, 4],
            svg.rect(
                x=-3,
                y=2,
                width=2,
                height=2,
                fill="red",
                opacity=0.8,
            ),
            svg.rect(
                x=1,
                y=2,
                width=2,
                height=2,
                fill="blue",
                opacity=0.8,
            ),
        )

        # Display the three worlds side by side
        return mo.hstack(
            [
                mo.Html(world1),
                mo.Html(world2),
                mo.Html(world3),
            ],
            justify="space-around",
        )


    # Run tests
    test_world()
    return (world,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Booster Drawing

    Create a `booster` function that:

    - takes the numeric arguments `x`, `y`, `theta` (in radians), `f` and `phi` (in radians)

    and returns

    - a SVG fragment that represents the body of the booster and the flame of its reactor.
    (The booster drawing can be very simple, for example a rectangle for the body and another one of a different color for the flame will be fine.)

    **Constraint:** make sure that

    - the orientation of the flame is correct,
    - its length is proportional to the force $f$,
    - the flame length is equal to $\ell/2$ when $f=Mg$.


    Test you function in the following scenarios:

    ```python
    mo.hstack(
        [
            mo.Html(
                world(
                    [-3, 3, -2, 4],
                    booster(0, l/2, 0, 0, 0),
                )
            ),
            mo.Html(
                world(
                    [-3, 3, -2, 4],
                    booster(0, l, 0, M * g, 0),
                )
            ),
            mo.Html(
                world(
                    [-3, 3, -2, 4],
                    booster(-l/2, l, np.pi / 4, 2 * M * g, np.pi / 2),
                )
            ),
        ],
        justify="space-around",
    )
    ```
    """)
    return


@app.cell
def _(M, g, l, mo, np, world):
    def booster(x, y, theta, f, phi):
        """
        Create an SVG fragment representing a rocket booster and its flame.
        """
        l = 2
        M = 1
        g = 1
        # ------------------------------------------------------------------
        # Geometry parameters
        # ------------------------------------------------------------------
        body_width = l / 6
        body_height = l

        # Flame length (scaled so that f = M*g → l/2)
        flame_length = (f / (M * g)) * (l / 2) if M * g != 0 else 0

        flame_width = body_width * 0.6

        # ------------------------------------------------------------------
        # Booster body
        # ------------------------------------------------------------------
        body = f'''
        <rect x="{-body_width/2}"
              y="{-body_height/2}"
              width="{body_width}"
              height="{body_height}"
              fill="#2C3E50"
              rx="{body_width/6}"/>
        '''

        # Nose cone
        nose = f'''
        <polygon points="
            {-body_width/2},{body_height/2}
            {body_width/2},{body_height/2}
            0,{body_height/2 + body_width/1.5}
        "
        fill="#34495E"/>
        '''

        # Flame
        if f > 0:
            flame = f'''
            <g transform="translate(0,{-body_height/2}) rotate({-phi * 180 / np.pi})">
                <polygon points="
                    {-flame_width/2},0
                    {flame_width/2},0
                    0,{-flame_length}
                "
                fill="#FF6600"
                opacity="0.85"/>
            </g>
            '''
        else:
            flame = ""

        # ------------------------------------------------------------------
        # Global transform
        # ------------------------------------------------------------------
        svg_fragment = f'''
        <g transform="translate({x},{y}) rotate({theta * 180 / np.pi})">
            {flame}
            {body}
            {nose}
        </g>
        '''

        return svg_fragment

    mo.hstack(
        [
            mo.Html(
                world(
                    [-3, 3, -2, 4],
                    booster(0, l/2, 0, 0, 0),
                )
            ),
            mo.Html(
                world(
                    [-3, 3, -2, 4],
                    booster(0, l, 0, M * g, 0),
                )
            ),
            mo.Html(
                world(
                    [-3, 3, -2, 4],
                    booster(-l/2, l, np.pi / 4, 2 * M * g, np.pi / 2),
                )
            ),
        ],
        justify="space-around",
    )
    
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Booster Animation

    Create a `booster_anim` function whose arguments are:

    - `x`, `y`, `theta` (in radians), `f` and `phi` (in radians)
    **which are functions of a time `t`**.
    - an animation duration `T`,

    and returns

    - a SVG fragment that represents the animated body of the booster and the flame of its reactor during `T` seconds, then repeats.
    (The booster drawing can be very simple, for example a rectangle for the body and another one of a different color for the flame will be fine.)

    **Constraint:** make sure that

    - the orientation of the flame is correct,
    - its length is proportional to the force $f$,
    - the flame length is equal to $\ell/2$ when $f=Mg$.

    Test your function in the following scenario:

    ```python
    def booster_anim_0():
        T = 5.0
        def x(t):
            return -l/2 + l * (t / T)
        def y(t):
            return l/2 + l/2 * (t / T)
        def theta(t):
            return (t / T) * 2 * np.pi
        def f(t):
            return M * g * (t / T)
        def phi(t):
            return 2 * np.pi * (t / T)
        return booster_anim(x, y, theta, f, phi, T=T)

    mo.Html(
        world([-3, 3, -2, 4], booster_anim_0())
    ).center()
    ```
    """)
    return


@app.cell
def _(M, g, l, mo, np, world):
    def booster_anim(x, y, theta, f, phi, T=5.0, frames=40):

        times = np.linspace(0, T, frames)

        # ------------------------------------------------------------
        # Build animation keyframes
        # ------------------------------------------------------------
        translate_vals = []
        rotate_vals = []
        flame_rotate_vals = []
        flame_length_vals = []

        for t in times:

            xt = x(t)
            yt = y(t)
            th = theta(t)

            ft = f(t)
            ph = phi(t)

            # Flame scaling rule
            flame_length = (ft / (M * g)) * (l / 2)

            translate_vals.append(f"{xt} {yt}")
            rotate_vals.append(f"{-th * 180 / np.pi}")
            flame_rotate_vals.append(f"{-ph * 180 / np.pi}")
            flame_length_vals.append(str(flame_length))

        translate_vals = ";".join(translate_vals)
        rotate_vals = ";".join(rotate_vals)
        flame_rotate_vals = ";".join(flame_rotate_vals)
        flame_length_vals = ";".join(flame_length_vals)

        # ------------------------------------------------------------
        # BODY
        # ------------------------------------------------------------
        body = f"""
        <g>

            <rect
                x="-0.125"
                y="-{l}"
                width="0.25"
                height="{2*l}"
                fill="gray"
                stroke="black"
                stroke-width="0.03"
                rx="0.05"
            />

            <!-- TRANSLATION -->
            <animateTransform
                attributeName="transform"
                type="translate"
                values="{translate_vals}"
                dur="{T}s"
                repeatCount="indefinite"
            />

            <!-- ROTATION -->
            <animateTransform
                attributeName="transform"
                type="rotate"
                values="{rotate_vals}"
                dur="{T}s"
                repeatCount="indefinite"
                additive="sum"
            />

        </g>
        """

        # ------------------------------------------------------------
        # FLAME
        # ------------------------------------------------------------
        flame = f"""
        <g>

            <polygon
                points="-0.08 -{l} 0.08 -{l} 0 -{l}"
                fill="orange"
                stroke="red"
                stroke-width="0.02"
            />

            <!-- TRANSLATION -->
            <animateTransform
                attributeName="transform"
                type="translate"
                values="{translate_vals}"
                dur="{T}s"
                repeatCount="indefinite"
            />

            <!-- ROTATION booster -->
            <animateTransform
                attributeName="transform"
                type="rotate"
                values="{rotate_vals}"
                dur="{T}s"
                repeatCount="indefinite"
                additive="sum"
            />

            <!-- ROTATION flame orientation -->
            <animateTransform
                attributeName="transform"
                type="rotate"
                values="{flame_rotate_vals}"
                dur="{T}s"
                repeatCount="indefinite"
                additive="sum"
            />

        </g>
        """

        return body + flame

    # ------------------------------------------------------------
    # TEST
    # ------------------------------------------------------------
    def booster_anim_0():

        T = 5.0
        M = 1
        g = 9.81
        l = 2

        def x(t):
            return -l / 2 + l * (t / T)

        def y(t):
            return l / 2 + l / 2 * (t / T)

        def theta(t):
            return (t / T) * 2 * np.pi

        def f(t):
            return M * g * (t / T)

        def phi(t):
            return 2 * np.pi * (t / T)

        return booster_anim(x, y, theta, f, phi, T=T)


    mo.Html(
        world(
            [-3, 3, -2, 4],
            booster_anim_0(),
        )
    ).center()
    return (booster_anim,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Animated Simulation Results

    Let's go back to a booster whose evolution is governed by its system of ordinary differentential equations. Produce a animation of the booster for 5 seconds for each of the following initial value problems:

    1. $(x, \dot{x}, y, \dot{y}, \theta, \dot{\theta}) = (0.0, 0.0, 10.0, 0.0, 0.0, 0.0)$, $f=0$ and $\phi=0$

    2. $(x, \dot{x}, y, \dot{y}, \theta, \dot{\theta}) = (0.0, 0.0, 10.0, 0.0, 0.0, 0.0)$, $f=Mg$ and $\phi=0$

    3. $(x, \dot{x}, y, \dot{y}, \theta, \dot{\theta}) = (0.0, 0.0, 10.0, 0.0, 0.0, 0.0)$, $f=Mg$ and $\phi=\pi/8$

    4. The "controlled landing" scenario (see above).
    """)
    return


@app.cell
def _(J, M, booster_anim, g, l, mo, np, world):
    # ------------------------------------------------------------
    # Simulate and animate several booster scenarios
    # Requires:
    #   - scipy.integrate.solve_ivp
    #   - booster_anim(x, y, theta, f, phi, T)
    #   - world(...)
    #   - mo
    # Global constants:
    #   - M, g, l, J
    # ------------------------------------------------------------

    from scipy.integrate import solve_ivp


    def simulate_booster(z0, f_fun, phi_fun, T=5.0, n=200):
        """
        Simulate the booster ODE.

        State:
            z = [x, vx, y, vy, theta, omega]
        """

        def ode(t, z):
            x, vx, y, vy, theta, omega = z

            f = f_fun(t)
            phi = phi_fun(t)

            # Translational dynamics
            ax = -(f / M) * np.sin(theta + phi)
            ay =  (f / M) * np.cos(theta + phi) - g

            # Rotational dynamics
            alpha = (l * f * np.sin(phi)) / J

            return [vx, ax, vy, ay, omega, alpha]

        t_eval = np.linspace(0, T, n)
        sol = solve_ivp(ode, [0, T], z0, t_eval=t_eval)

        return sol


    def solution_to_functions(sol):
        """
        Convert solve_ivp solution into callable functions.
        """

        def interp_component(i):
            def func(t):
                t_mod = t % sol.t[-1]
                return np.interp(t_mod, sol.t, sol.y[i])
            return func

        x = interp_component(0)
        y = interp_component(2)
        theta = interp_component(4)

        return x, y, theta


    def make_animation(z0, f_fun, phi_fun, T=5.0):
        """
        Simulate then create SVG animation.
        """
        sol = simulate_booster(z0, f_fun, phi_fun, T=T)
        x, y, theta = solution_to_functions(sol)

        return booster_anim(x, y, theta, f_fun, phi_fun, T=T)


    # ------------------------------------------------------------
    # Initial condition
    # (x, vx, y, vy, theta, omega)
    # ------------------------------------------------------------
    z0 = [0.0, 0.0, 10.0, 0.0, 0.0, 0.0]


    # ------------------------------------------------------------
    # Scenario 1: Free fall (f = 0, phi = 0)
    # ------------------------------------------------------------
    def f1(t):
        return 0.0


    def phi1(t):
        return 0.0


    # ------------------------------------------------------------
    # Scenario 2: Hover (f = M*g, phi = 0)
    # ------------------------------------------------------------
    def f2(t):
        return M * g


    def phi2(t):
        return 0.0


    # ------------------------------------------------------------
    # Scenario 3: Tilted thrust (f = M*g, phi = pi/8)
    # ------------------------------------------------------------
    def f3(t):
        return M * g


    def phi3(t):
        return np.pi / 8


    # ------------------------------------------------------------
    # Scenario 4: Controlled landing
    # ------------------------------------------------------------
    def f4(t):
        # Slightly stronger than weight near the end
        if t < 3.5:
            return 0.8 * M * g
        else:
            return 1.2 * M * g


    def phi4(t):
        # Stabilizing oscillation
        return 0.15 * np.sin(2 * np.pi * t / 5.0)


    # ------------------------------------------------------------
    # Build animations
    # ------------------------------------------------------------
    anim1 = make_animation(z0, f1, phi1, T=5.0)
    anim2 = make_animation(z0, f2, phi2, T=5.0)
    anim3 = make_animation(z0, f3, phi3, T=5.0)
    anim4 = make_animation(z0, f4, phi4, T=5.0)


    # ------------------------------------------------------------
    # Display all scenarios
    # ------------------------------------------------------------
    mo.hstack(
        [
            mo.Html(world([-15, 15, 0, 15], anim1)),
            mo.Html(world([-15, 15, 0, 15], anim2)),
            mo.Html(world([-15, 15, 0, 15], anim3)),
            mo.Html(world([-15, 15, 0, 15], anim4)),
        ],
        justify="space-around",
    )
    return


if __name__ == "__main__":
    app.run()
