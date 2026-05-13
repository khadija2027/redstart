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

    return la, np, plt, sci, scipy


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

    Define the Python constants `g`, `M` and `l` that correspond to the gravity constant, the mass and length of the booster.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### 🔓 Solution
    """)
    return


@app.cell(hide_code=True)
def _():
    g = 1.0
    M = 1.0
    l = 2
    return M, g, l


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Forces

    Compute the cartesian coordinates $f_x$ and $f_y$ of the force applied to the booster by the reactor, as functions of $f$, $\theta$ and $\phi$.
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    ### 🔓 Solution
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Given the geometric setting, the cartesian coordinates of the unit vector $\vec{u}=(u_x, u_y)$ aligned with the reactor (or flame) axis and pointing from the reactor towards the flame satisfy:

    \begin{align*}
    u_x & = +\sin (\theta + \phi) \\
    u_y & = -\cos(\theta +\phi)
    \end{align*}

    Assuming that $f \geq 0$, the force applied to the booster is in the opposite direction and has amplitude $f$:

    $$
    \vec{f} = -f \vec{u}
    $$

    Therefore,

    \begin{align*}
    f_x & = -f \sin (\theta + \phi) \\
    f_y & = +f \cos(\theta +\phi)
    \end{align*}
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Center of Mass

    Give the ordinary differential equation that governs the evolution of the position $(x, y)$ of the center of mass of the booster.
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    ### 🔓 Solution
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The force exerted by the gravity on the booster is

    $$
    \vec{f}_g =
    \begin{bmatrix}
    0 \\ - M g
    \end{bmatrix}
    $$

    By Newton's second law of motion, the acceleration $\vec{a} = (\ddot{x}, \ddot{y})$
    satisfies $M \vec{a} = \vec{f} + \vec{f}_g$ and thus

    \begin{align*}
    M \ddot{x} & = -f \sin (\theta + \phi) \\
    M \ddot{y} & = +f \cos(\theta +\phi) - Mg
    \end{align*}
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Moment of inertia

    Compute the [moment of inertia](https://en.wikipedia.org/wiki/Moment_of_inertia) $J$ of the booster and define the corresponding Python variable `J`.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 🔓 Solution

    The moment of inertia of a thin rod with uniformly distributed mass about its center is of mass is

    $$
    J = \frac{1}{12} M \ell^2
    $$
    """)
    return


@app.cell
def _(M, l):
    J = M * l ** 2 / 12
    J
    return (J,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Tilt

    Give the ordinary differential equation that governs the evolution of the tilt angle $\theta$.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 🔓 Solution

    Newton's Second Law for Rotation is $J \ddot{\theta} = \tau$ where $\tau$ is the torque applied to the booster. Here the torque applied by the gravity to the booster is $0$ by symmetry and only the booster reactor induces a torque. The torque can be
    first computed as a vector in 3D as the cross-product of the vector between the center of the booster and the reactor location and the force applied by the reactor.
    Afterwards, we can be project it on the 3rd axis to get $\tau$.

    Thus, we have

    $$
    \tau =
    \left(
    \ell / 2
    \begin{bmatrix}
    {} +\sin \theta \\ - \cos \theta \\ 0
    \end{bmatrix}
    \wedge \begin{bmatrix} -f \sin (\theta + \phi) \\ +f \cos (\theta + \phi) \\ 0
    \end{bmatrix}
    \right)
    \cdot \begin{bmatrix} 0 \\ 0 \\ 1 \end{bmatrix}
    =
    \ell/2 (f\sin \theta \cos (\theta + \phi) - f\sin (\theta + \phi) \cos \theta).
    $$

    Since $\sin \alpha \cos \beta - \sin \beta \cos \alpha = \sin (\alpha - \beta)$,
    we obtain

    $$
    \tau = - f (\ell/2) \sin \phi,
    $$

    thus the angular acceleration is governed by

    $$
    J \ddot{\theta} = - f (\ell / 2)  \sin \phi.
    $$
    """)
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


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 🔓 Solution

    Given that

    \begin{align*}
    M \ddot{x} & = -f \sin (\theta + \phi) \\
    M \ddot{y} & = +f \cos(\theta +\phi) - Mg \\
    J \ddot{\theta} & = - f (\ell/2) \sin \phi
    \end{align*}

    and $\dot{x} = v_x$, $\dot{y} = v_y$ and $\dot{\theta} = \omega$, we
    can use as a state vector $s = (x, v_x, y, v_y, \theta, \omega) \in \mathbb{R}^6$
    and the corresponding function $F$ is given by

    $$
    F(s, f, \phi) = \begin{bmatrix}
    v_x \\ -(f / M) \sin (\theta + \phi) \\
    v_y \\ +(f / M) \cos(\theta +\phi) - g \\
    \omega \\ - (f / J) (\ell/2) \sin \phi
    \end{bmatrix}
    $$
    """)
    return


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


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### 🔓 Solution
    """)
    return


@app.cell(hide_code=True)
def _(J, M, g, l, np, scipy):
    def redstart_solve(t_span, y0, f_phi):
        def fun(t, state):
            x, vx, y, vy, theta, omega = state
            f, phi = f_phi(t, state)
            d2x = (-f * np.sin(theta + phi)) / M
            d2y = (+ f * np.cos(theta + phi)) / M - g
            d2theta = - (f / J) * (l / 2) * np.sin(phi)
            return np.array([vx, d2x, vy, d2y, omega, d2theta])
        r = scipy.integrate.solve_ivp(fun, t_span, y0, dense_output=True)
        return r.sol

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


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 🔓 Solution

    In the free fall scenario, the solution satisfies $x(t)=0$, $y(t) = y(0) - g/2 t^2$ and $\theta(t) = 0$. Since numerically $y(0)=10.0$, $g=1$ and $\ell=2$, the threshold
    is crossed when $10 - 1/2 t^2 = 2$, that is $t=4$.
    """)
    return


@app.cell(hide_code=True)
def _(l, np, plt, redstart_solve):
    def free_fall_example():
        t_span = [0.0, 5.0]
        y0 = [0.0, 0.0, 10.0, 0.0, 0.0, 0.0]  # [x, vx, y, vy, theta, omega]

        def f_phi(t, y):
            return np.array([0.0, 0.0])  # [f, phi]
        sol = redstart_solve(t_span, y0, f_phi)
        t = np.linspace(t_span[0], t_span[1], 1000)
        y_t = sol(t)[2]
        plt.plot(t, y_t, label=r"$y(t)$ (height in meters)")
        plt.plot(t, l * np.ones_like(t), color="grey",
                 ls="--", label=r"$y=\ell$")
        plt.title("Free Fall")
        plt.xlabel("time $t$")
        plt.grid(True)
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


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### 🔓 Solution
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We can search for a cubic polynomial

    $$
    y(t) = a_3 t^3 + a_2 t^2 + a_1 t + a_0
    $$

    that solves the four given constraints,
    then deduce $f(t)$ from the equation $M \ddot{y} = f + Mg$.

    The time derivative of $y$ satisfies
    $$
    \dot{y}(t) = 3 a_3 t^2 + 2 a_2 t + a_1,
    $$
    thus the constraints are:

    \begin{align*}
    y(0) = a_0 &= 10, \\
    \dot{y}(0) = a_1 &= -2,\\
    y(5) = 125 a_3 + 25 a_2 + 5 a_1 + a_0 &= 1, \\
    \dot{y}(5) = 75 a_3 + 10 a_2 + a_1 &= 0. \\
    \end{align*}

    The solution of this linear system provides:

    $$
    y(t)
    =\frac{8}{125}t^3 - \frac{7}{25} t^2 - 2t + 10,
    $$
    which yields
    $$
    \ddot{y}(t)
    =
    \frac{48}{125}t - \frac{14}{25}
    $$
    and therefore since $M=1$ and $g=1$,
    $$
    f(t) = \frac{\ddot{y}(t)}{M} + g = \frac{48}{125}t + \frac{11}{25}.
    $$
    """)
    return


@app.cell(hide_code=True)
def _(l, np, plt, redstart_solve):
    def controlled_landing_example():
        t_span = [0.0, 5.0]
        y0 = [0.0, 0.0, 10.0, -2.0, 0.0, 0.0]

        def f_phi_smooth_landing(t, state):
            return np.array([48 / 125 * t + 11 / 25, 0])
        sol = redstart_solve(t_span, y0, f_phi=f_phi_smooth_landing)
        t = np.linspace(t_span[0], t_span[1], 1000)
        y_t = sol(t)[2]
        plt.plot(t, y_t, label=r"$y(t)$ (height in meters)")
        plt.plot(t, (l / 2) * np.ones_like(t),
                 color="grey", ls="--", label=r"$y=\ell/2$")
        plt.title("Controlled Landing")
        plt.xlabel("time $t$")
        plt.grid(True)
        plt.legend()
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

    return animate_transform, svg, transform


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


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### 🔓 Solution
    """)
    return


@app.cell
def _(svg, transform):
    def world(view_box, *objects):
        x_min, x_max, y_min, y_max = view_box
        width, height = x_max - x_min, y_max - y_min

        return svg.svg(
            xmlns="http://www.w3.org/2000/svg",
            viewBox=f"0 0 {width} {height}",
            style="max-height:80vh")(
            transform.translate(x=-x_min, y=y_max)(
                transform.scale(y=-1.0)(
                    # Sky
                    svg.rect(x=-1e3, y=0, width=2e3,
                             height=1e3, fill="lightskyblue"),
                    # Ground
                    svg.rect(x=-1e3, y=-2e3, width=2e3,
                             height=2e3, fill="sandybrown"),
                    # Target
                    svg.rect(x=-1, y=-1, width=2,
                             height=1, fill="lightgreen"),
                    *objects,
                )
            )
        )

    return (world,)


@app.cell
def _(mo, svg, world):
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
    return


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


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### 🔓 Solution
    """)
    return


@app.cell
def _(M, g, l, np, svg, transform):
    def booster(x, y, theta, f, phi):
        flame_length = (l / 2) * (f / M / g)
        return transform.translate(x, y)(
            transform.rotate(theta / np.pi * 180.0)(
                svg.rect(x=-l/20, y=-l/2, width=l/10, height=l, fill="black"),
                transform.translate(0, -l / 2)(
                    transform.rotate(phi / np.pi * 180)(
                        svg.rect(
                            x=-l/20,
                            y=-flame_length,
                            width=l/10,
                            height=flame_length,
                            fill="red",
                        )
                    )
                )
            )
        )

    return (booster,)


@app.cell(hide_code=True)
def _(M, booster, g, l, mo, np, world):
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


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### 🔓 Solution
    """)
    return


@app.cell
def _(M, animate_transform, g, l, np, svg):
    def booster_anim(x, y, theta, f, phi, T):
        if not callable(theta):
            theta_cst = theta
            def theta(t): return theta_cst
        if not callable(phi):
            phi_cst = phi
            def phi(t): return phi_cst

        def theta_deg(t):
            return theta(t) / np.pi * 180.0

        def phi_deg(t):
            return phi(t) / np.pi * 180.0

        return animate_transform.translate(x, y, T=T)(
            animate_transform.rotate(theta_deg, T=T)(
                svg.rect(
                    x=-l / 20,
                    y=-l/2,
                    width=l / 10,
                    height=l,
                    fill="black",
                ),
                animate_transform.translate(y=-l/2, T=T)(
                    animate_transform.rotate(phi_deg, T=T)(
                        animate_transform.scale(y=f, T=T)(
                            svg.rect(
                                x=-l/20,
                                y=-1/M/g,
                                width=l / 10,
                                height=1/M/g,
                                fill="red",
                            )
                        )
                    )
                ),
            )
        )

    return (booster_anim,)


@app.cell
def _(M, booster_anim, g, l, np):
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

    return (booster_anim_0,)


@app.cell
def _(booster_anim_0, mo, world):
    mo.Html(
        world([-3, 3, -2, 4], booster_anim_0())
    ).center()
    return


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


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### 🔓 Solution
    """)
    return


@app.cell
def _(booster_anim, mo, np, redstart_solve, world):
    def anim_1():
        t_span = [0.0, 5.0]
        y0 = [0.0, 0.0, 10.0, 0.0, 0.0, 0.0]

        def f_phi(t, state):
            return np.array([0, 0])
        sol = redstart_solve(t_span, y0, f_phi)
        def x(t): return sol(t)[0]
        def y(t): return sol(t)[2]
        def theta(t): return sol(t)[4]
        def f(t): return f_phi(t, sol(t))[0]
        def phi(t): return f_phi(t, sol(t))[0]
        return mo.Html(
            world(
                [-3, 3, -2, 12],
                booster_anim(x, y, theta, f, phi, T=t_span[1])
            )
        ).center()

    anim_1()
    return


@app.cell
def _(M, booster_anim, g, mo, np, redstart_solve, world):
    def anim_2():
        t_span = [0.0, 5.0]
        y0 = [0.0, 0.0, 10.0, 0.0, 0.0, 0.0]

        def f_phi(t, state):
            return np.array([M * g, 0])
        sol = redstart_solve(t_span, y0, f_phi)
        def x(t): return sol(t)[0]
        def y(t): return sol(t)[2]
        def theta(t): return sol(t)[4]
        def f(t): return f_phi(t, sol(t))[0]
        def phi(t): return f_phi(t, sol(t))[1]
        return mo.Html(
            world(
                [-3, 3, -2, 12],
                booster_anim(x, y, theta, f, phi, T=t_span[1])
            )
        ).center()

    anim_2()
    return


@app.cell
def _(M, booster_anim, g, mo, np, redstart_solve, world):
    def anim_3():
        t_span = [0.0, 5.0]
        y0 = [0.0, 0.0, 10.0, 0.0, 0.0, 0.0]

        def f_phi(t, state):
            return np.array([M * g, np.pi / 8])
        sol = redstart_solve(t_span, y0, f_phi)
        def x(t): return sol(t)[0]
        def y(t): return sol(t)[2]
        def theta(t): return sol(t)[4]
        def f(t): return f_phi(t, sol(t))[0]
        def phi(t): return f_phi(t, sol(t))[1]
        return mo.Html(
            world(
                [-3, 3, -2, 12],
                booster_anim(x, y, theta, f, phi, T=t_span[1])
            )
        ).center()

    anim_3()
    return


@app.cell
def _(booster_anim, mo, np, redstart_solve, world):
    def anim_4():
        t_span = [0.0, 5.0]
        y0 = [0.0, 0.0, 10.0, -2.0, 0.0, 0.0]

        def f_phi(t, state):
            return np.array([48 / 125 * t + 11 / 25, 0])
        sol = redstart_solve(t_span, y0, f_phi)
        def x(t): return sol(t)[0]
        def y(t): return sol(t)[2]
        def theta(t): return sol(t)[4]
        def f(t): return f_phi(t, sol(t))[0]
        def phi(t): return f_phi(t, sol(t))[1]
        return mo.Html(
            world(
                [-3, 3, -2, 12],
                booster_anim(x, y, theta, f, phi, T=t_span[1])
            )
        ).center()

    anim_4()
    return


@app.cell
def _(mo):
    mo.md(r"""
    # Linearized Dynamics
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Equilibria

    We assume that

    - $|\theta| < \pi/2$,
    - $|\phi| < \pi/2$, and
    - $f > 0$.

    What are the possible equilibria of the system for constant inputs $f$ and $\phi$ and what are the corresponding values of these inputs?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### 🔓 Solution
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Our state is $s = (x, v_x, y, v_y,\theta, \omega)$ and the system is governed by
    $\dot{s} = F(s, f, \phi)$ with
    $$
    F(s, f, \phi) = \begin{bmatrix}
    v_x \\ -(f / M) \sin (\theta + \phi) \\
    v_y \\ +(f / M) \cos(\theta +\phi) - g \\
    \omega \\ - (f / J) (\ell/2) \sin \phi
    \end{bmatrix}
    $$
    The equilibria are characterized by $F(s, f, \phi) = 0$. We obtain directly that
    $v_x = v_y = 0$ and $\omega = 0$. We also extract the two equations

    $$
    \begin{bmatrix}
    -(f / M) \sin (\theta + \phi) \\
    +(f / M) \cos(\theta +\phi)
    \end{bmatrix}
    =
    \begin{bmatrix}
    0 \\
    g
    \end{bmatrix}
    $$
    which holds if when $|\theta| < \pi/2$ and $|\phi| < \pi/2$ and only if
    $\theta = \phi = 0$ and $f = M g$. The final equation is then satisfied if and only if
    $\omega = 0$. Finally, we obtain the equilibria as:
    $$
    \begin{bmatrix}
    x \\
    v_x \\
    y \\
    v_y \\
    \theta \\
    \omega \\
    f \\
    \phi
    \end{bmatrix}
    =
    \begin{bmatrix}
    ? \\
    0 \\
    ? \\
    0 \\
    0 \\
    0 \\
    M g \\
    0
    \end{bmatrix}
    $$
    where $?$ stands for "any possible value".
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Linearized Model

    Introduce the error variables $\Delta x$, $\Delta y$, $\Delta \theta$, and $\Delta f$ and $\Delta \phi$ of the state and input values with respect to the generic equilibrium configuration.
    What are the linear ordinary differential equations that govern (approximately) these variables in a neighbourhood of the equilibrium?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### 🔓 Solution
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We have $\Delta \theta = \theta$, $\Delta \phi = \phi$ and $\Delta f = f - M g$. Given that

    \begin{align*}
    M \ddot{x} & = -f \sin (\theta + \phi) \\
    M \ddot{y} & = +f \cos(\theta +\phi) - Mg \\
    J \ddot{\theta} & = - f (\ell/2) \sin \phi
    \end{align*}

    and that for small values of $\alpha$, $\sin \alpha \approx \alpha$ and $\cos \alpha \approx 1$, we obtain:

    \begin{align*}
    M (d/dt)^2 \Delta x &= - Mg (\Delta \theta + \Delta \phi)  \\
    M (d/dt)^2 \Delta y &= \Delta f \\
    J (d/dt)^2 \Delta \theta &= - (Mg \ell /2) \Delta \phi \\
    \end{align*}
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Standard Form

    1. What are the matrices $A$ and $B$ associated to this linear model in standard form?
    2. Define the corresponding NumPy arrays `A` and `B`.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 🔓 Solution
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Note: remember that $J = (1/12) M \ell^2$.

    $$
    A =
    \begin{bmatrix}
    0 & 1 & 0 & 0 & 0  & 0 \\
    0 & 0 & 0 & 0 & -g & 0 \\
    0 & 0 & 0 & 1 & 0  & 0 \\
    0 & 0 & 0 & 0 & 0  & 0 \\
    0 & 0 & 0 & 0 & 0  & 1 \\
    0 & 0 & 0 & 0 & 0  & 0
    \end{bmatrix}
    \;\;\;
    B =
    \begin{bmatrix}
    0 & 0\\
    0 & -g\\
    0 & 0\\
    1/M & 0\\
    0 & 0 \\
    0 & -M g \ell/(2J)\\
    \end{bmatrix}
    =
    \begin{bmatrix}
    0 & 0\\
    0 & -g\\
    0 & 0\\
    1/M & 0\\
    0 & 0 \\
    0 & - 6 g / \ell\\
    \end{bmatrix}
    $$
    """)
    return


@app.cell(hide_code=True)
def _(g, np):
    A = np.zeros((6, 6))
    A[0, 1] = 1.0
    A[1, 4] = -g
    A[2, 3] = 1.0
    A[4, -1] = 1.0
    A
    return (A,)


@app.cell(hide_code=True)
def _(M, g, l, np):
    B = np.zeros((6, 2))
    B[1, 1] = -g
    B[3, 0] = 1/M
    B[-1, 1] = -6 * g / l
    B
    return (B,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Stability

    Is the generic equilibrium asymptotically stable?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 🔓 Solution

    No, since $0$ is the only eigenvalue of $A$ and $0$ doesn't have a negative real part.
    """)
    return


@app.cell(hide_code=True)
def _(A, la):
    eigenvalues, eigenvectors = la.eig(A)
    print(f"Eigenvalues of A: {eigenvalues}")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Controllability

    Is the linearized model controllable?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 🔓 Solution

    The controllability matrix of the system is:
    """)
    return


@app.cell(hide_code=True)
def _(A, B, np):
    # Controllability
    cs = np.column_stack
    mp = np.linalg.matrix_power
    KC = cs([mp(A, k) @ B for k in range(6)])
    KC
    return (KC,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    and its rank is
    """)
    return


@app.cell(hide_code=True)
def _(KC, np):
    int(np.linalg.matrix_rank(KC))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    which is equal to the state dimension, so the answer is yes, it's controllable.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Lateral Dynamics

    We limit our interest in the lateral position $x$, the tilt $\theta$ and their derivatives (we are for the moment fine with letting $y$ and $\dot{y}$ be uncontrolled). We also set $f = M g$ and control the system only with $\phi$.

    - What are the new (reduced) matrices $A$ and $B$ for this reduced system?

    - Check the controllability of this new system.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 🔓 Solution
    """)
    return


@app.cell
def _(g, l, np):
    A_lat = np.array([
        [0, 1, 0, 0],
        [0, 0, -g, 0],
        [0, 0, 0, 1],
        [0, 0, 0, 0]], dtype=np.float64)
    B_lat = np.array([[0, -g, 0, - 6 * g / l]]).T

    print("A_lat:")
    print(A_lat)
    print("B_lat:")
    print(B_lat)
    return A_lat, B_lat


@app.cell(hide_code=True)
def _(A_lat, B_lat, np):
    # Controllability
    _cs = np.column_stack
    _mp = np.linalg.matrix_power
    KC_lat = _cs([_mp(A_lat, k) @ B_lat for k in range(6)])
    KC_lat
    return (KC_lat,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    This reduced system of dimension 4 is controllable since the rank of its controllability matrix is 4:
    """)
    return


@app.cell(hide_code=True)
def _(KC_lat, np):
    np.linalg.matrix_rank(KC_lat)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Linear Model in Free Fall

    Make graphs of $x(t)$ and $\theta(t)$ for the linearized model when
    - $x(0)=0$, $\dot{x}(0)=0$, $\theta(0) = \pi/4$, $\dot{\theta}(0) =0$, and
    - $\phi(t)=0$ at all times.

    What do you see? How do you explain it?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 🔓 Solution
    """)
    return


@app.cell(hide_code=True)
def _(g, l, np):
    def make_fun_lat(phi):
        def fun_lat(t, state):
            x, dx, theta, dtheta = state
            phi_ = phi(t, state)
            d2x = -g * (theta + phi_)
            d2theta = - 6 * g / l * phi_
            return np.array([dx, d2x, dtheta, d2theta])

        return fun_lat

    return (make_fun_lat,)


@app.cell(hide_code=True)
def _(make_fun_lat, mo, np, plt, sci):
    def lin_sim_1():
        def phi(t, state):
            return 0.0

        f_lat = make_fun_lat(phi)
        t_span = [0, 10]
        state_0 = [0, 0, 45 * np.pi / 180.0, 0]
        r = sci.solve_ivp(
            fun=f_lat, y0=state_0, t_span=t_span, dense_output=True
        )
        t = np.linspace(t_span[0], t_span[1], 1000)
        sol_t = r.sol(t)
        fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True)
        ax1.plot(t, sol_t[0], label=r"$x(t)$")
        ax1.grid(True)
        ax1.legend()
        ax2.plot(t, sol_t[2], label=r"$\theta(t)$")
        ax2.grid(True)
        ax2.set_xlabel(r"time $t$")
        ax2.legend()
        return mo.center(fig)

    lin_sim_1()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    - Since the reactor pushes (with a constant force) in the axis of the booster ($\phi=0$) and the initial title velocity $\omega = \dot{\theta}$ is zero, it's sensible that the title $\theta$ stays constant. That explains the second graph.
    - On the other hand, the constant projected force on the $x$-axis drives a constant acceleration which is towards the left since the initial tilt is positive. That explain the first graph.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Manually Tuned Controller

    Try to find the two missing coefficients of the matrix

    $$
    K =
    \begin{bmatrix}
    0 & 0 & ? & ?
    \end{bmatrix}
    \in \mathbb{R}^{4\times 1}
    $$

    such that the control law

    $$
    \Delta \phi(t) = - K \cdot
    \begin{bmatrix}
    \Delta x(t) \\
    \Delta \dot{x}(t) \\
    \Delta \theta(t) \\
    \Delta \dot{\theta}(t)
    \end{bmatrix} \in \mathbb{R}
    $$

    manages  when
    $\Delta x(0)=0$, $\Delta \dot{x}(0)=0$, $\Delta \theta(0) = 45 / 180  \times \pi$  and $\Delta \dot{\theta}(0) =0$ to:

    - make $\Delta \theta(t) \to 0$ in approximately $20$ sec (or less),
    - $|\Delta \theta(t)| < \pi/2$ and $|\Delta \phi(t)| < \pi/2$ at all times,
    - (but we don't care about a possible drift of $\Delta x(t)$).

    Explain your thought process, show your iterative guesses and simulations!

    Is your final closed-loop model asymptotically stable?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### 🔓 Solution
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We try first a controller that corrects using only $\Delta \theta$ since it it's the simples think we can think of (a controller based only on the derivative would not achieve $\Delta \theta(t) \to 0$ since it would only knows $\Delta \theta(t)$ up to a constant). When $\Delta \theta > 0$, we want the reactor to be oriented on the right ($\Delta \phi > 0$) to compensate for this trend.

    Hence it makes sens to start for something simple such as
    $\Delta \phi =  \Delta \theta$, which corresponds to

    $$
    K =
    \begin{bmatrix}
    0 & 0 & -1 & 0
    \end{bmatrix}
    \in \mathbb{R}^{4\times 1}
    $$

    and

    $$
    \Delta \phi(t) = - K \cdot
    \begin{bmatrix}
    \Delta x(t) \\
    \Delta \dot{x}(t) \\
    \Delta \theta(t) \\
    \Delta \dot{\theta}(t)
    \end{bmatrix} \in \mathbb{R}
    $$

    Let's make a simulation out of this!
    """)
    return


@app.cell
def _(A_lat, B_lat, make_fun_lat, mo, np, plt, sci):
    def lin_sim_k1():

        K = np.array([0.0, 0.0, -1.0, 0.0])

        print(
            "eigenvalues:",
            np.linalg.eig(
                A_lat - B_lat.reshape((-1, 1)) @ K.reshape((1, -1))
            ).eigenvalues,
        )

        t_span = [0, 20.0]
        t = np.linspace(t_span[0], t_span[1], 1000)
        state_0 = [0, 0, 45 * np.pi / 180.0, 0]

        def phi(t, state):
            return -K.dot(state)

        f_lat = make_fun_lat(phi)
        r = sci.solve_ivp(fun=f_lat, y0=state_0,
                          t_span=t_span, dense_output=True)
        sol_lin_t = r.sol(t)

        fig, (ax1, ax2, ax3) = plt.subplots(3, 1, sharex=True, figsize=(12, 6))
        ax1.plot(t, sol_lin_t[0], label=r"$x(t)$ (lin.)")
        ax1.grid(True)
        ax1.legend(loc="lower right")
        ax2.plot(t, sol_lin_t[2], label=r"$\theta(t)$ (lin.)")
        ax2.plot(t, 0.5 * np.pi * np.ones_like(t), "r--", label=r"$\pm\pi/2$")
        ax2.plot(t, -0.5 * np.pi * np.ones_like(t), "r--")
        ax2.grid(True)
        ax2.legend(loc="lower right")
        ax3.plot(t, phi(t, sol_lin_t), label=r"$\phi(t)$ (lin.)")
        ax3.grid(True)
        ax3.plot(t, 0.5 * np.pi * np.ones_like(t), "r--", label=r"$\pm\pi/2$")
        ax3.plot(t, -0.5 * np.pi * np.ones_like(t), "r--")
        ax3.set_xlabel(r"time $t$")
        ax3.legend(loc="lower right")
        return mo.center(fig)

    lin_sim_k1()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Unfortunately that doesn't work, we have introduced an oscillatory dynamics.

    To correct that, we may introduce some additionial "friction" that prevents our compensation to kick in too fast and end up the control
    $\Delta \phi = \Delta \theta + \beta (d \Delta \theta /dt)$, for some $\beta > 0$, which corresponds to

    $$
    K =
    \begin{bmatrix}
    0 & 0 & -1 & -\beta
    \end{bmatrix}
    \in \mathbb{R}^{4\times 1}
    $$

    Experimentally (see below), anything between $\beta = 0.1$ and $\beta = 5.0$ seems to satisfy the specification. The closed-loop dynamics is slower need $0.1$ and faster near $5.0$.

    In any case, there is a permament drift which is induced on $\Delta x$, which does not converge to $0$. This is corroborated by a double eigenvalue at $0$, which proves that our closed-loop dynamics is **not** asymptotically stable.
    """)
    return


@app.cell(hide_code=True)
def _(A_lat, B_lat, make_fun_lat, mo, np, plt, sci):
    def lin_sim_k2():

        K = np.array([0.0, 0.0, -1.0, -0.1])

        print(
            "eigenvalues:",
            np.linalg.eig(
                A_lat - B_lat.reshape((-1, 1)) @ K.reshape((1, -1))
            ).eigenvalues,
        )

        t_span = [0, 20.0]
        t = np.linspace(t_span[0], t_span[1], 1000)
        state_0 = [0, 0, 45 * np.pi / 180.0, 0]

        def phi(t, state):
            return -K.dot(state)

        f_lat = make_fun_lat(phi)
        r = sci.solve_ivp(fun=f_lat, y0=state_0,
                          t_span=t_span, dense_output=True)
        sol_lin_t = r.sol(t)

        fig, (ax1, ax2, ax3) = plt.subplots(3, 1, sharex=True, figsize=(12, 6))
        ax1.plot(t, sol_lin_t[0], label=r"$x(t)$ (lin.)")
        ax1.grid(True)
        ax1.legend(loc="lower right")
        ax2.plot(t, sol_lin_t[2], label=r"$\theta(t)$ (lin.)")
        ax2.plot(t, 0.5 * np.pi * np.ones_like(t), "r--", label=r"$\pm\pi/2$")
        ax2.plot(t, -0.5 * np.pi * np.ones_like(t), "r--")
        ax2.grid(True)
        ax2.legend(loc="lower right")
        ax3.plot(t, phi(t, sol_lin_t), label=r"$\phi(t)$ (lin.)")
        ax3.grid(True)
        ax3.plot(t, 0.5 * np.pi * np.ones_like(t), "r--", label=r"$\pm\pi/2$")
        ax3.plot(t, -0.5 * np.pi * np.ones_like(t), "r--")
        ax3.set_xlabel(r"time $t$")
        ax3.legend(loc="lower right")
        return mo.center(fig)

    lin_sim_k2()
    return


@app.cell
def _(A_lat, B_lat, make_fun_lat, mo, np, plt, sci):
    def lin_sim_k3():

        K = np.array([0.0, 0.0, -1.0, -5.0])

        print(
            "eigenvalues:",
            np.linalg.eig(
                A_lat - B_lat.reshape((-1, 1)) @ K.reshape((1, -1))
            ).eigenvalues,
        )

        t_span = [0, 20.0]
        t = np.linspace(t_span[0], t_span[1], 1000)
        state_0 = [0, 0, 45 * np.pi / 180.0, 0]

        def phi(t, state):
            return -K.dot(state)

        f_lat = make_fun_lat(phi)
        r = sci.solve_ivp(fun=f_lat, y0=state_0,
                          t_span=t_span, dense_output=True)
        sol_lin_t = r.sol(t)

        fig, (ax1, ax2, ax3) = plt.subplots(3, 1, sharex=True, figsize=(12, 6))
        ax1.plot(t, sol_lin_t[0], label=r"$x(t)$ (lin.)")
        ax1.grid(True)
        ax1.legend(loc="lower right")
        ax2.plot(t, sol_lin_t[2], label=r"$\theta(t)$ (lin.)")
        ax2.plot(t, 0.5 * np.pi * np.ones_like(t), "r--", label=r"$\pm\pi/2$")
        ax2.plot(t, -0.5 * np.pi * np.ones_like(t), "r--")
        ax2.grid(True)
        ax2.legend(loc="lower right")
        ax3.plot(t, phi(t, sol_lin_t), label=r"$\phi(t)$ (lin.)")
        ax3.grid(True)
        ax3.plot(t, 0.5 * np.pi * np.ones_like(t), "r--", label=r"$\pm\pi/2$")
        ax3.plot(t, -0.5 * np.pi * np.ones_like(t), "r--")
        ax3.set_xlabel(r"time $t$")
        ax3.legend(loc="lower right")
        return mo.center(fig)

    lin_sim_k3()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Controller Tuned with Pole Assignment

    Using pole assignement, find a matrix

    $$
    K_{pp} =
    \begin{bmatrix}
    ? & ? & ? & ?
    \end{bmatrix}
    \in \mathbb{R}^{4\times 1}
    $$

    such that the control law

    $$
    \Delta \phi(t)
    = - K_{pp} \cdot
    \begin{bmatrix}
    \Delta x(t) \\
    \Delta \dot{x}(t) \\
    \Delta \theta(t) \\
    \Delta \dot{\theta}(t)
    \end{bmatrix} \in \mathbb{R}
    $$

    satisfies the conditions defined for the manually tuned controller and additionally:

    - result in an asymptotically stable closed-loop dynamics,

    - make $\Delta x(t) \to 0$ in approximately $20$ sec (or less).

    Explain how you find the proper design parameters!
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### 🔓 Solution
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We decide to try to cluster all our eigenvalue near a single real (negative) value
    $s$. If we want a convergence at 5% in 20 seconds at most, we know that $|\lambda|$
    should be at least $3 / 20 = 0.15$.

    Experimentally however this is a bit slow to converge (see below), the setup is better if we pick a faster dynamics, to have our eigenvalues clustered around $-0.5$ for example.

    There is actually quite a range of locations that work, but around $-0.1$, we start compensating too fast and to violate the constraint on the maximal value of $\phi$.
    """)
    return


@app.cell
def _(A_lat, B_lat, make_fun_lat, mo, np, plt, sci, scipy):
    def lin_sim_3():
        K = scipy.signal.place_poles(
            A=A_lat,
            B=B_lat,
            poles=-0.15 * np.array([1.0, 1.01, 1.02, 1.03]),
        ).gain_matrix.squeeze()

        print(f"K = {K}")

        print(
            "eigenvalues:",
            np.linalg.eig(
                A_lat - B_lat.reshape((-1, 1)) @ K.reshape((1, -1))
            ).eigenvalues,
        )

        t_span = [0, 20.0]
        t = np.linspace(t_span[0], t_span[1], 1000)
        state_0 = [0, 0, 45 * np.pi / 180.0, 0]

        def phi(t, state):
            return -K.dot(state)

        f_lat = make_fun_lat(phi)
        r = sci.solve_ivp(fun=f_lat, y0=state_0,
                          t_span=t_span, dense_output=True)
        sol_lin_t = r.sol(t)

        fig, (ax1, ax2, ax3) = plt.subplots(3, 1, sharex=True, figsize=(12, 6))
        ax1.plot(t, sol_lin_t[0], label=r"$x(t)$ (lin.)")
        ax1.grid(True)
        ax1.legend(loc="lower right")
        ax2.plot(t, sol_lin_t[2], label=r"$\theta(t)$ (lin.)")
        ax2.plot(t, 0.5 * np.pi * np.ones_like(t), "r--", label=r"$\pm\pi/2$")
        ax2.plot(t, -0.5 * np.pi * np.ones_like(t), "r--")
        ax2.grid(True)
        ax2.legend(loc="lower right")
        ax3.plot(t, phi(t, sol_lin_t), label=r"$\phi(t)$ (lin.)")
        ax3.grid(True)
        ax3.plot(t, 0.5 * np.pi * np.ones_like(t), "r--", label=r"$\pm\pi/2$")
        ax3.plot(t, -0.5 * np.pi * np.ones_like(t), "r--")
        ax3.set_xlabel(r"time $t$")
        ax3.legend(loc="lower right")
        return mo.center(fig)

    lin_sim_3()
    return


@app.cell
def _(A_lat, B_lat, make_fun_lat, mo, np, plt, sci, scipy):
    Kpp = scipy.signal.place_poles(
        A=A_lat,
        B=B_lat,
        poles=-0.5 * np.array([1.0, 1.01, 1.02, 1.03]),
    ).gain_matrix.squeeze()

    def lin_sim_32():
        K = Kpp
        print(f"K = {K}")

        print(
            "eigenvalues:",
            np.linalg.eig(
                A_lat - B_lat.reshape((-1, 1)) @ K.reshape((1, -1))
            ).eigenvalues,
        )

        t_span = [0, 20.0]
        t = np.linspace(t_span[0], t_span[1], 1000)
        state_0 = [0, 0, 45 * np.pi / 180.0, 0]

        def phi(t, state):
            return -K.dot(state)

        f_lat = make_fun_lat(phi)
        r = sci.solve_ivp(fun=f_lat, y0=state_0,
                          t_span=t_span, dense_output=True)
        sol_lin_t = r.sol(t)

        fig, (ax1, ax2, ax3) = plt.subplots(3, 1, sharex=True, figsize=(12, 6))
        ax1.plot(t, sol_lin_t[0], label=r"$x(t)$ (lin.)")
        ax1.grid(True)
        ax1.legend(loc="lower right")
        ax2.plot(t, sol_lin_t[2], label=r"$\theta(t)$ (lin.)")
        ax2.plot(t, 0.5 * np.pi * np.ones_like(t), "r--", label=r"$\pm\pi/2$")
        ax2.plot(t, -0.5 * np.pi * np.ones_like(t), "r--")
        ax2.grid(True)
        ax2.legend(loc="lower right")
        ax3.plot(t, phi(t, sol_lin_t), label=r"$\phi(t)$ (lin.)")
        ax3.grid(True)
        ax3.plot(t, 0.5 * np.pi * np.ones_like(t), "r--", label=r"$\pm\pi/2$")
        ax3.plot(t, -0.5 * np.pi * np.ones_like(t), "r--")
        ax3.set_xlabel(r"time $t$")
        ax3.legend(loc="lower right")
        return mo.center(fig)

    lin_sim_32()
    return (Kpp,)


@app.cell
def _(A_lat, B_lat, make_fun_lat, mo, np, plt, sci, scipy):
    def lin_sim_33():
        K = scipy.signal.place_poles(
            A=A_lat,
            B=B_lat,
            poles=-1.0 * np.array([1.0, 1.01, 1.02, 1.03]),
        ).gain_matrix.squeeze()

        print(f"K = {K}")

        print(
            "eigenvalues:",
            np.linalg.eig(
                A_lat - B_lat.reshape((-1, 1)) @ K.reshape((1, -1))
            ).eigenvalues,
        )

        t_span = [0, 20.0]
        t = np.linspace(t_span[0], t_span[1], 1000)
        state_0 = [0, 0, 45 * np.pi / 180.0, 0]

        def phi(t, state):
            return -K.dot(state)

        f_lat = make_fun_lat(phi)
        r = sci.solve_ivp(fun=f_lat, y0=state_0,
                          t_span=t_span, dense_output=True)
        sol_lin_t = r.sol(t)

        fig, (ax1, ax2, ax3) = plt.subplots(3, 1, sharex=True, figsize=(12, 6))
        ax1.plot(t, sol_lin_t[0], label=r"$x(t)$ (lin.)")
        ax1.grid(True)
        ax1.legend(loc="lower right")
        ax2.plot(t, sol_lin_t[2], label=r"$\theta(t)$ (lin.)")
        ax2.plot(t, 0.5 * np.pi * np.ones_like(t), "r--", label=r"$\pm\pi/2$")
        ax2.plot(t, -0.5 * np.pi * np.ones_like(t), "r--")
        ax2.grid(True)
        ax2.legend(loc="lower right")
        ax3.plot(t, phi(t, sol_lin_t), label=r"$\phi(t)$ (lin.)")
        ax3.grid(True)
        ax3.plot(t, 0.5 * np.pi * np.ones_like(t), "r--", label=r"$\pm\pi/2$")
        ax3.plot(t, -0.5 * np.pi * np.ones_like(t), "r--")
        ax3.set_xlabel(r"time $t$")
        ax3.legend(loc="lower right")
        return mo.center(fig)

    lin_sim_33()
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## 🧩 Controller Tuned with Optimal Control

    Using optimal control, find a gain matrix $K_{oc}$ that satisfies the same set of requirements that the one defined using pole placement.

    Explain how you find the proper design parameters!
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### 🔓 Solution
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The basic optimal control design, with

    $$
    Q = \begin{bmatrix}
    1 & 0 & 0 & 0 \\
    0 & 0 & 0 & 0 \\
    0 & 0 & 1 & 0 \\
    0 & 0 & 0 & 1
    \end{bmatrix},
    $$

    and

    $$
    R = \begin{bmatrix}
    1
    \end{bmatrix},
    $$
    almost makes the job, except that it is a bit too fast and that results initially in large values of the angle $\phi$.
    """)
    return


@app.cell
def _(A_lat, B_lat, make_fun_lat, mo, np, plt, sci, scipy):
    def lin_sim_4():
        Q = np.eye(4, 4)
        print("Q:", Q)
        R = np.eye(1)  # 10*l**2 * np.eye(1)
        print("R:", R)
        Pi = scipy.linalg.solve_continuous_are(
            a=A_lat,
            b=B_lat,
            q=Q,
            r=R
        )
        Koc = (np.linalg.inv(R) @ B_lat.T @ Pi).squeeze()

        K = Koc
        print(f"K = {K}")

        print(
            "eigenvalues:",
            np.linalg.eig(
                A_lat - B_lat.reshape((-1, 1)) @ K.reshape((1, -1))
            ).eigenvalues,
        )

        t_span = [0, 20.0]
        t = np.linspace(t_span[0], t_span[1], 1000)
        state_0 = [0, 0, 45 * np.pi / 180.0, 0]

        def phi(t, state):
            return -K.dot(state)

        f_lat = make_fun_lat(phi)
        r = sci.solve_ivp(fun=f_lat, y0=state_0,
                          t_span=t_span, dense_output=True)
        sol_lin_t = r.sol(t)

        fig, (ax1, ax2, ax3) = plt.subplots(3, 1, sharex=True, figsize=(12, 6))
        ax1.plot(t, sol_lin_t[0], label=r"$x(t)$ (lin.)")
        ax1.grid(True)
        ax1.legend(loc="lower right")
        ax2.plot(t, sol_lin_t[2], label=r"$\theta(t)$ (lin.)")
        ax2.plot(t, 0.5 * np.pi * np.ones_like(t), "r--", label=r"$\pm\pi/2$")
        ax2.plot(t, -0.5 * np.pi * np.ones_like(t), "r--")
        ax2.grid(True)
        ax2.legend(loc="lower right")
        ax3.plot(t, phi(t, sol_lin_t), label=r"$\phi(t)$ (lin.)")
        ax3.grid(True)
        ax3.plot(t, 0.5 * np.pi * np.ones_like(t), "r--", label=r"$\pm\pi/2$")
        ax3.plot(t, -0.5 * np.pi * np.ones_like(t), "r--")
        ax3.set_xlabel(r"time $t$")
        ax3.legend(loc="lower right")
        return mo.center(fig)

    lin_sim_4()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    A second design with the same $Q$ but $R$ increased by $100$ (to reduce the activation of the input at the price of some convergence speed) performs adequately!
    """)
    return


@app.cell
def _(A_lat, B_lat, make_fun_lat, mo, np, plt, sci, scipy):
    Q = np.eye(4, 4)
    print("Q:", Q)
    R = 100 * np.eye(1)
    print("R:", R)
    Pi = scipy.linalg.solve_continuous_are(
        a=A_lat,
        b=B_lat,
        q=Q,
        r=R
    )
    Koc = (np.linalg.inv(R) @ B_lat.T @ Pi).squeeze()

    def lin_sim_42():
        K = Koc
        print(f"K = {K}")

        print(
            "eigenvalues:",
            np.linalg.eig(
                A_lat - B_lat.reshape((-1, 1)) @ K.reshape((1, -1))
            ).eigenvalues,
        )

        t_span = [0, 20.0]
        t = np.linspace(t_span[0], t_span[1], 1000)
        state_0 = [0, 0, 45 * np.pi / 180.0, 0]

        def phi(t, state):
            return -K.dot(state)

        f_lat = make_fun_lat(phi)
        r = sci.solve_ivp(fun=f_lat, y0=state_0,
                          t_span=t_span, dense_output=True)
        sol_lin_t = r.sol(t)

        fig, (ax1, ax2, ax3) = plt.subplots(3, 1, sharex=True, figsize=(12, 6))
        ax1.plot(t, sol_lin_t[0], label=r"$x(t)$ (lin.)")
        ax1.grid(True)
        ax1.legend(loc="lower right")
        ax2.plot(t, sol_lin_t[2], label=r"$\theta(t)$ (lin.)")
        ax2.plot(t, 0.5 * np.pi * np.ones_like(t), "r--", label=r"$\pm\pi/2$")
        ax2.plot(t, -0.5 * np.pi * np.ones_like(t), "r--")
        ax2.grid(True)
        ax2.legend(loc="lower right")
        ax3.plot(t, phi(t, sol_lin_t), label=r"$\phi(t)$ (lin.)")
        ax3.grid(True)
        ax3.plot(t, 0.5 * np.pi * np.ones_like(t), "r--", label=r"$\pm\pi/2$")
        ax3.plot(t, -0.5 * np.pi * np.ones_like(t), "r--")
        ax3.set_xlabel(r"time $t$")
        ax3.legend(loc="lower right")
        return mo.center(fig)

    lin_sim_42()
    return (Koc,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Validation

    Test the two control strategies (pole placement and optimal control) on the "true" (nonlinear) model with an animation. Check that both controllers achieve their goal; otherwise, go back to the drawing board and tweak the design parameters until they do!
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### 🔓 Solution
    """)
    return


@app.cell(hide_code=True)
def _(Kpp, M, booster_anim, g, mo, np, redstart_solve, world):
    def _anim():
        t_span = [0.0, 20.0]
        y0 = [0.0, 0.0, 20.0, 0.0, 45 * np.pi/180.0, 0.0]

        def f_phi(t, state):
            x, dx, y, dy, theta, dtheta = state
            return np.array(
                [M*g, -Kpp.dot([x, dx, theta, dtheta])]
            )
        sol = redstart_solve(t_span, y0, f_phi)
        def x(t): return sol(t)[0]
        def y(t): return sol(t)[2]
        def theta(t): return sol(t)[4]
        def f(t): return f_phi(t, sol(t))[0]
        def phi(t): return f_phi(t, sol(t))[1]
        return mo.Html(
            world(
                [-6, 6, -2, 22],
                booster_anim(x, y, theta, f, phi, T=t_span[1])
            )
        ).center()

    _anim()
    return


@app.cell(hide_code=True)
def _(Koc, M, booster_anim, g, mo, np, redstart_solve, world):
    def _anim():
        t_span = [0.0, 20.0]
        y0 = [0.0, 0.0, 20.0, 0.0, 45 * np.pi/180.0, 0.0]

        def f_phi(t, state):
            x, dx, y, dy, theta, dtheta = state
            return np.array(
                [M*g, -Koc.dot([x, dx, theta, dtheta])]
            )
        sol = redstart_solve(t_span, y0, f_phi)
        def x(t): return sol(t)[0]
        def y(t): return sol(t)[2]
        def theta(t): return sol(t)[4]
        def f(t): return f_phi(t, sol(t))[0]
        def phi(t): return f_phi(t, sol(t))[1]
        return mo.Html(
            world(
                [-6, 6, -2, 22],
                booster_anim(x, y, theta, f, phi, T=t_span[1])
            )
        ).center()

    _anim()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Exact Linearization

    Let
    $$
    R(\alpha) =
    \begin{bmatrix} +\cos \alpha & -\sin \alpha \\ +\sin \alpha & +\cos \alpha
    \end{bmatrix}
    $$

    Consider an auxiliary system which is meant to compute the force $(f_x, f_y)$ applied to the booster.

    The inputs of the auxiliary system are

    $$
    v = (v_1, v_2) \in \mathbb{R}^2,
    $$

    its dynamics

    $$
    \ddot{z} = v_1 \qquad \text{ where } \qquad z \in \mathbb{R}
    $$

    and its output $(f_x, f_y) \in \mathbb{R}^2$ is given by

    \[
    \begin{bmatrix}
    f_x \\
    f_y
    \end{bmatrix} = R\left(\theta - \frac{\pi}{2}\right)
    \begin{bmatrix}
    z - M\ell\dot{\theta}^2 / 6 \\
    {M\ell v_2}/{6z}
    \end{bmatrix}
    \]

    ⚠️ Note that the second component $f_y$ of the reactor force is undefined whenever $z=0$.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Geometrical Interpretation


    Consider the output $h$ of the original system

    $$
    h :=
    \begin{bmatrix}
    x - (\ell/6) \sin \theta \\
    y + (\ell/6) \cos \theta
    \end{bmatrix} \in \mathbb{R}^2
    $$

    Provide a geometrical interpretation of $h$ (for example, make a drawing).
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    The output $h$ is the position of a specific point on the booster body, located
    at a distance $\ell/6$ from the center of mass, in the direction opposite to the nozzle

    The unit vector pointing from the nozzle towards the top of the booster is:
    $$
    \begin{bmatrix} -\sin\theta \\ +\cos\theta \end{bmatrix}
    $$
    so the point at distance $\ell/6$ from the center of mass in that direction has coordinates:
    $$
    h = \begin{bmatrix} x \\ y \end{bmatrix} + \frac{\ell}{6}
    \begin{bmatrix} -\sin\theta \\ +\cos\theta \end{bmatrix}
    =
    \begin{bmatrix} x - (\ell/6)\sin\theta \\ y + (\ell/6)\cos\theta \end{bmatrix}.
    $$

    Since the booster has total length $\ell$, its center of mass is at $\ell/2$ from each end.
    The point $h$ is therefore located at:
    $$
    \frac{\ell}{2} - \frac{\ell}{6} = \frac{\ell}{3}
    $$
    """)
    return


@app.cell
def _(M, booster, g, l, mo, np, svg, transform, world):
    _theta = np.pi / 7
    _x, _y = 0.0, 2.5

    _hx = _x - (l/6) * np.sin(_theta)
    _hy = _y + (l/6) * np.cos(_theta)

    _drawing = world(
        [-3, 3, -1, 5],
        booster(_x, _y, _theta, M * g, 0),
        # center of mass dot
        transform.translate(_x, _y)(
            svg.circle(r=0.08, fill="blue")
        ),
        # h point dot
        transform.translate(_hx, _hy)(
            svg.circle(r=0.08, fill="red")
        ),
        # CoM label
        transform.translate(_x + 0.12, _y)(
            transform.scale(1, -1)(
                svg.text(fill="blue", style="font-size:0.18px")("Center of Mass (x, y)")
            )
        ),
        # h label
        transform.translate(_hx + 0.12, _hy)(
            transform.scale(1, -1)(
                svg.text(fill="red", style="font-size:0.18px")("h")
            )
        ),
    )
    mo.Html(_drawing).center()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 First and Second-Order Derivatives

    Compute $\dot{h}$ as a function of $\dot{x}$, $\dot{y}$, $\theta$ and $\dot{\theta}$ (and constants) and then $\ddot{h}$ as a function of $\theta$ and $z$ (and constants) when the auxiliary system is plugged in the booster.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### 🔓 Solution

    **First derivative:**

    $$
    \dot{h} = \begin{bmatrix} \dot{x} + \frac{\ell}{6}\dot{\theta}\cos\theta \\ \dot{y} - \frac{\ell}{6}\dot{\theta}\sin\theta \end{bmatrix}
    $$

    **Second derivative.** Using $R(\theta - \pi/2) = \begin{bmatrix}\sin\theta & \cos\theta \\ -\cos\theta & \sin\theta\end{bmatrix}$, the auxiliary system gives:

    $$f_x = \sin\theta\!\left(z - \tfrac{M\ell\dot\theta^2}{6}\right) + \tfrac{M\ell v_2}{6}\cos\theta, \qquad f_y = -\cos\theta\!\left(z - \tfrac{M\ell\dot\theta^2}{6}\right) + \tfrac{M\ell v_2}{6}\sin\theta$$

    and the torque equation gives $\ddot\theta = -v_2$. Substituting $M\ddot{x} = f_x$, $M\ddot{y} = f_y - Mg$, the $v_2$ and $\dot\theta^2$ terms cancel exactly and:

    $$\ddot{h} = \frac{z}{M}\begin{bmatrix}\sin\theta \\ -\cos\theta\end{bmatrix} - \begin{bmatrix}0 \\ g\end{bmatrix}$$
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Third and Fourth-Order Derivatives

    Compute the third derivative $h^{(3)}$ of $h$ as a function of $\theta$ and $z$ (and constants) and then the fourth derivative $h^{(4)}$ of $h$ with respect to time as a function of $\theta$, $\dot{\theta}$, $z$, $\dot{z}$, $v$ (and constants) when the auxiliary system is on.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### 🔓 Solution

    **Third derivative.** Differentiating $\ddot{h}$:

    $$h^{(3)} = \frac{1}{M}\begin{bmatrix}\sin\theta & \cos\theta \\ -\cos\theta & \sin\theta\end{bmatrix}\begin{bmatrix}\dot{z} \\ z\dot{\theta}\end{bmatrix}$$

    **Fourth derivative.** Differentiating $h^{(3)}$ and using $\ddot{z} = v_1$, $\ddot\theta = v_2/z$:

    Since $\frac{d}{dt}\begin{bmatrix}\dot{z} \\ z\dot{\theta}\end{bmatrix} = \begin{bmatrix}v_1 \\ \dot{z}\dot{\theta} + z\ddot{\theta}\end{bmatrix} = \begin{bmatrix}v_1 \\ \dot{z}\dot{\theta} + v_2\end{bmatrix}$,

    we obtain:

    $$h^{(4)} = \frac{1}{M}\begin{bmatrix}\sin\theta & \cos\theta \\ -\cos\theta & \sin\theta\end{bmatrix}\begin{bmatrix}v_1 - z\dot\theta^2 \\ 2\dot{z}\dot\theta + v_2\end{bmatrix}$$
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Exact Linearization

    Show that with yet another auxiliary system with input $u=(u_1, u_2)$ and output $v$ fed into the previous one, we can achieve the dynamics

    $$
    h^{(4)} = u
    $$
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### 🔓 Solution

    From the previous part:

    $$
    h^{(4)} = \frac{1}{M}
    \begin{bmatrix}\sin\theta & \cos\theta \\ -\cos\theta & \sin\theta\end{bmatrix}
    \begin{bmatrix}
        v_1 - z\dot{\theta}^2 \\
        2\dot{z}\dot{\theta} + v_2
    \end{bmatrix}
    $$

    **Choosing $v$ to achieve $h^{(4)} = u$.**

    Since the matrix $\begin{bmatrix}\sin\theta & \cos\theta \\ -\cos\theta & \sin\theta\end{bmatrix}$ is a rotation matrix, it is invertible with transpose as its inverse. Setting $h^{(4)} = u$:

    $$
    \begin{bmatrix}
        v_1 - z\dot{\theta}^2 \\
        2\dot{z}\dot{\theta} + v_2
    \end{bmatrix}
    = M\begin{bmatrix}\sin\theta & -\cos\theta \\ \cos\theta & \sin\theta\end{bmatrix} u
    $$

    Denoting $\begin{bmatrix}w_1 \\ w_2\end{bmatrix} = M\begin{bmatrix}\sin\theta & -\cos\theta \\ \cos\theta & \sin\theta\end{bmatrix} u$, the second auxiliary system is:

    $$
    \boxed{
    v_1 = z\dot{\theta}^2 + w_1,
    \qquad
    v_2 = w_2 - 2\dot{z}\dot{\theta},
    \qquad
    \begin{bmatrix}w_1\\w_2\end{bmatrix} = M \begin{bmatrix}\sin\theta & -\cos\theta \\ \cos\theta & \sin\theta\end{bmatrix} u.
    }
    $$

    With this choice, $h^{(4)} = u$ exactly. The overall system is therefore equivalent to **two independent chains of four integrators**:

    $$
    h_x^{(4)} = u_1, \qquad h_y^{(4)} = u_2,
    $$

    which is a fully linearized and decoupled system.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 State to Derivatives of the Output

    Implement a function `Tr` of `x, dx, y, dy, theta, dtheta, z, dz` that returns `h_x, h_y, dh_x, dh_y, d2h_x, d2h_y, d3h_x, d3h_y`.
    """)
    return


@app.cell
def _(M, g, l, np):
    def Tr(x, dx, y, dy, theta, dtheta, z, dz):
        M_val = 1.0  # or use M from context

        # h
        h_x = x - (l/6) * np.sin(theta)
        h_y = y + (l/6) * np.cos(theta)

        # dh/dt
        dh_x = dx - (l/6) * dtheta * np.cos(theta)
        dh_y = dy - (l/6) * dtheta * np.sin(theta)

        # d2h/dt2
        # From: d2h = (z/M) * [sin(theta), -cos(theta)]^T - [0, g]^T
        d2h_x = (z / M) * np.sin(theta)
        d2h_y = -(z / M) * np.cos(theta) - g

        # d3h/dt3
        # From: h^(3) = (1/M) * R(theta) * [dz, z*dtheta]^T
        d3h_x = (1/M) * (np.sin(theta) * dz + np.cos(theta) * z * dtheta)
        d3h_y = (1/M) * (-np.cos(theta) * dz + np.sin(theta) * z * dtheta)

        return h_x, h_y, dh_x, dh_y, d2h_x, d2h_y, d3h_x, d3h_y

    return (Tr,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Inversion


    Assume for the sake of simplicity that $z<0$ at all times. Show that given the values of $h$, $\dot{h}$, $\ddot{h}$ and $h^{(3)}$, one can uniquely compute the booster state (the values of $x$, $\dot{x}$, $y$, $\dot{y}$, $\theta$, $\dot{\theta}$) and auxiliary system state (the values of $z$ and $\dot{z}$).

    Implement the corresponding function `T_inv`.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### 🔓 Solution

    We have four vector quantities available:
    $h, \dot{h}, \ddot{h}, h^{(3)} \in \mathbb{R}^2$,
    giving 8 scalar equations to recover 8 unknowns
    $(x, \dot{x}, y, \dot{y}, \theta, \dot{\theta}, z, \dot{z})$.

    **Step 1 — recover $z$ and $\theta$ from $\ddot{h}$.**

    From:
    $$\ddot{h} = \frac{z}{M}\begin{bmatrix}\sin\theta \\ -\cos\theta\end{bmatrix} - \begin{bmatrix}0 \\ g\end{bmatrix}$$

    we isolate the gravity term:
    $$\frac{z}{M}\begin{bmatrix}\sin\theta \\ -\cos\theta\end{bmatrix} = \ddot{h} + \begin{bmatrix}0 \\ g\end{bmatrix}$$

    Taking the Euclidean norm and using $z < 0$:
    $$\frac{|z|}{M} = \left\|\ddot{h} + \begin{bmatrix}0 \\ g\end{bmatrix}\right\| \quad\Longrightarrow\quad \boxed{z = -M\left\|\ddot{h} + \begin{bmatrix}0 \\ g\end{bmatrix}\right\|}$$

    The angle $\theta$ follows from the direction of the vector:
    $$\boxed{\theta = \operatorname{atan2}\!\left(\ddot{h}_x,\; -(\ddot{h}_y + g)\right)}$$

    **Step 2 — recover $\dot{z}$ and $\dot{\theta}$ from $h^{(3)}$.**

    From:
    $$h^{(3)} = \frac{1}{M}\begin{bmatrix}\sin\theta & \cos\theta \\ -\cos\theta & \sin\theta\end{bmatrix}\begin{bmatrix}\dot{z} \\ z\dot{\theta}\end{bmatrix}$$

    Inverting the rotation matrix:
    $$\begin{bmatrix}\dot{z} \\ z\dot{\theta}\end{bmatrix} = M\begin{bmatrix}\sin\theta & -\cos\theta \\ \cos\theta & \sin\theta\end{bmatrix}\begin{bmatrix}h^{(3)}_x \\ h^{(3)}_y\end{bmatrix}$$

    Therefore:
    $$\boxed{\dot{z} = M\!\left(\sin\theta\; h^{(3)}_x - \cos\theta\; h^{(3)}_y\right)}$$
    $$\boxed{\dot{\theta} = \frac{M}{z}\!\left(\cos\theta\; h^{(3)}_x + \sin\theta\; h^{(3)}_y\right)}$$

    **Step 3 — recover $(x, y)$ from $h$.**

    $$\boxed{x = h_x + \frac{\ell}{6}\sin\theta, \qquad y = h_y - \frac{\ell}{6}\cos\theta}$$

    **Step 4 — recover $(\dot{x}, \dot{y})$ from $\dot{h}$.**

    $$\boxed{\dot{x} = \dot{h}_x + \frac{\ell}{6}\dot{\theta}\cos\theta, \qquad \dot{y} = \dot{h}_y + \frac{\ell}{6}\dot{\theta}\sin\theta}$$
    """)
    return


@app.cell
def _(M, g, l, np):
    def T_inv(h_x, h_y, dh_x, dh_y, d2h_x, d2h_y, d3h_x, d3h_y):

        # Step 1: z and theta from d2h
        vec_x = d2h_x
        vec_y = d2h_y + g

        norm = np.sqrt(vec_x**2 + vec_y**2)
        z = -M * norm
        theta = np.arctan2(vec_x, -vec_y)

        # Step 2: dz and dtheta from d3h
        cos_t, sin_t = np.cos(theta), np.sin(theta)

        dz     = M * ( sin_t * d3h_x - cos_t * d3h_y)
        dtheta = (M / z) * ( cos_t * d3h_x + sin_t * d3h_y)

        # Step 3: x, y from h
        x = h_x + (l/6) * sin_t
        y = h_y - (l/6) * cos_t

        # Step 4: dx, dy from dh
        dx = dh_x + (l/6) * dtheta * cos_t
        dy = dh_y + (l/6) * dtheta * sin_t

        return x, dx, y, dy, theta, dtheta, z, dz

    return (T_inv,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Admissible Path Computation

    Implement a function

    ```python
    def compute(
        x_0,
        dx_0,
        y_0,
        dy_0,
        theta_0,
        dtheta_0,
        z_0,
        dz_0,
        x_tf,
        dx_tf,
        y_tf,
        dy_tf,
        theta_tf,
        dtheta_tf,
        z_tf,
        dz_tf,
        tf,
    ):
        ...

    ```

    that returns a function `fun` such that `fun(t)` is a value of `x, dx, y, dy, theta, dtheta, z, dz, f, phi` at time `t` that match the initial and final values provided as arguments to `compute`.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### 🔓 Solution

    We need to find a path that matches the initial and final conditions on
    $(x, \dot{x}, y, \dot{y}, \theta, \dot{\theta}, z, \dot{z})$.

    The key idea is to work in the $h$-coordinates. Using `Tr`, we convert the
    initial and final booster states into initial and final conditions on
    $h, \dot{h}, \ddot{h}, h^{(3)}$. Then, since $h^{(4)} = u$, each component
    of $h$ satisfies a **chain of 4 integrators**: we just need to find a
    polynomial of degree 7 (with 8 coefficients) matching the 4 boundary
    conditions at $t=0$ and $t=t_f$ for each component independently.
    Finally, we convert back to booster coordinates using `T_inv`.
    """)
    return


@app.cell
def _(M, T_inv, Tr, g, l, np):
    def compute(
        x_0, dx_0, y_0, dy_0, theta_0, dtheta_0, z_0, dz_0,
        x_tf, dx_tf, y_tf, dy_tf, theta_tf, dtheta_tf, z_tf, dz_tf,
        tf,
    ):
        # --- Convert initial and final states to h-coordinates ---
        h_x0, h_y0, dh_x0, dh_y0, d2h_x0, d2h_y0, d3h_x0, d3h_y0 = Tr(
            x_0, dx_0, y_0, dy_0, theta_0, dtheta_0, z_0, dz_0
        )
        h_xf, h_yf, dh_xf, dh_yf, d2h_xf, d2h_yf, d3h_xf, d3h_yf = Tr(
            x_tf, dx_tf, y_tf, dy_tf, theta_tf, dtheta_tf, z_tf, dz_tf
        )

        # --- Fit a degree-7 polynomial for each component of h ---
        # p(t) = a0 + a1*t + a2*t^2 + ... + a7*t^7
        # 8 conditions: p(0), p'(0), p''(0), p'''(0),
        #               p(tf), p'(tf), p''(tf), p'''(tf)

        def poly_coeffs(h0, dh0, d2h0, d3h0, hf, dhf, d2hf, d3hf, tf):
            # Build the 8x8 linear system
            T  = tf
            T2 = T**2;  T3 = T**3;  T4 = T**4
            T5 = T**5;  T6 = T**6;  T7 = T**7

            A = np.array([
                # p(0)
                [1, 0,  0,   0,    0,    0,    0,    0   ],
                # p'(0)
                [0, 1,  0,   0,    0,    0,    0,    0   ],
                # p''(0)
                [0, 0,  2,   0,    0,    0,    0,    0   ],
                # p'''(0)
                [0, 0,  0,   6,    0,    0,    0,    0   ],
                # p(tf)
                [1, T,  T2,  T3,   T4,   T5,   T6,   T7  ],
                # p'(tf)
                [0, 1,  2*T, 3*T2, 4*T3, 5*T4, 6*T5, 7*T6],
                # p''(tf)
                [0, 0,  2,   6*T,  12*T2,20*T3,30*T4,42*T5],
                # p'''(tf)
                [0, 0,  0,   6,    24*T, 60*T2,120*T3,210*T4],
            ])
            b = np.array([h0, dh0, d2h0, d3h0, hf, dhf, d2hf, d3hf])
            return np.linalg.solve(A, b)

        cx = poly_coeffs(h_x0, dh_x0, d2h_x0, d3h_x0,
                         h_xf, dh_xf, d2h_xf, d3h_xf, tf)
        cy = poly_coeffs(h_y0, dh_y0, d2h_y0, d3h_y0,
                         h_yf, dh_yf, d2h_yf, d3h_yf, tf)

        # --- Evaluate polynomial and its derivatives ---
        def eval_poly(c, t):
            # value
            p   = sum(c[k] * t**k for k in range(8))
            # 1st derivative
            dp  = sum(k * c[k] * t**(k-1) for k in range(1, 8))
            # 2nd derivative
            d2p = sum(k*(k-1) * c[k] * t**(k-2) for k in range(2, 8))
            # 3rd derivative
            d3p = sum(k*(k-1)*(k-2) * c[k] * t**(k-3) for k in range(3, 8))
            return p, dp, d2p, d3p

        # --- Build the output function ---
        def fun(t):
            t = np.asarray(t, dtype=float)
            scalar = t.ndim == 0
            t = np.atleast_1d(t)

            results = []
            for ti in t:
                hx,  dhx,  d2hx,  d3hx  = eval_poly(cx, ti)
                hy,  dhy,  d2hy,  d3hy  = eval_poly(cy, ti)

                x, dx, y, dy, theta, dtheta, z, dz = T_inv(
                    hx, hy, dhx, dhy, d2hx, d2hy, d3hx, d3hy
                )

                # Recover f and phi from z, theta, dtheta
                # f_x = -f*sin(theta+phi), f_y = f*cos(theta+phi)
                # From auxiliary system: f = sqrt(fx^2 + fy^2)
                # Here we use: z relates to the normal force
                f   = np.sqrt(
                    (z - M*l*dtheta**2/6)**2 +
                    0.0  # phi=0 on the reference path approximation
                )
                # More precisely, recover f and phi from (fx, fy):
                # fx = -f*sin(theta+phi), fy = f*cos(theta+phi) - M*g... 
                # use the booster equations directly:
                # M*d2x = fx, M*(d2y+g) = fy
                d2hx_val, d2hy_val = d2hx, d2hy
                # accelerations of CoM
                # d2x_com and d2y_com come from h:
                # d2h = (z/M)*[sin theta, -cos theta] - [0,g]
                fx =  z * np.sin(theta)
                fy = -z * np.cos(theta) - M*g + M*g   # simplifies
                fy = -z * np.cos(theta)

                f_norm = np.sqrt(fx**2 + fy**2)
                phi = np.arctan2(-fx, fy) - theta

                results.append([x, dx, y, dy, theta, dtheta, z, dz, f_norm, phi])

            out = np.array(results).T
            return out[:, 0] if scalar else out

        return fun

    return (compute,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Graphical Validation

    Test your `compute` function with

    - `(x_0, dx_0, y_0, dy_0, theta_0, dtheta_0, z_0, dz_0) = (5.0, 0.0, 20.0, -1.0, -np.pi/8, 0.0, -M*g, 0.0`),
    - `(x_tf, dx_tf, y_tf, dy_tf, theta_tf, dtheta_tf, z_tf, dz_tf) = (0.0, 0.0, 2/3*l, 0.0,     0.0, 0.0, -M*g, 0.0`),
    - `tf = 10.0`.

    Make the graph of the relevant variables as a function of time, then make an animation out of the same result. Comment and iterate if necessary!
    """)
    return


@app.cell
def _(M, compute, g, l, mo, np, plt):
    def graphical_validation():
        # Initial and final conditions
        x_0, dx_0      = 5.0,  0.0
        y_0, dy_0      = 20.0, -1.0
        theta_0        = -np.pi/8
        dtheta_0       = 0.0
        z_0, dz_0      = -M*g, 0.0

        x_tf, dx_tf    = 0.0,  0.0
        y_tf, dy_tf    = 2/3*l, 0.0
        theta_tf       = 0.0
        dtheta_tf      = 0.0
        z_tf, dz_tf    = -M*g, 0.0

        tf = 10.0

        fun = compute(
            x_0, dx_0, y_0, dy_0, theta_0, dtheta_0, z_0, dz_0,
            x_tf, dx_tf, y_tf, dy_tf, theta_tf, dtheta_tf, z_tf, dz_tf,
            tf,
        )

        t = np.linspace(0, tf, 1000)
        sol = fun(t)

        x, dx, y, dy, theta, dtheta, z, dz, f, phi = sol

        fig, axes = plt.subplots(5, 2, figsize=(12, 14), sharex=True)
        fig.suptitle("Admissible Path — Graphical Validation", fontsize=14)

        axes[0,0].plot(t, x);         axes[0,0].set_ylabel(r"$x$");         axes[0,0].grid(True)
        axes[0,1].plot(t, dx);        axes[0,1].set_ylabel(r"$\dot{x}$");   axes[0,1].grid(True)
        axes[1,0].plot(t, y);         axes[1,0].set_ylabel(r"$y$");         axes[1,0].grid(True)
        axes[1,1].plot(t, dy);        axes[1,1].set_ylabel(r"$\dot{y}$");   axes[1,1].grid(True)
        axes[2,0].plot(t, theta);     axes[2,0].set_ylabel(r"$\theta$");    axes[2,0].grid(True)
        axes[2,0].plot(t,  np.pi/2 * np.ones_like(t), "r--")
        axes[2,0].plot(t, -np.pi/2 * np.ones_like(t), "r--")
        axes[2,1].plot(t, dtheta);    axes[2,1].set_ylabel(r"$\dot\theta$");axes[2,1].grid(True)
        axes[3,0].plot(t, z);         axes[3,0].set_ylabel(r"$z$");         axes[3,0].grid(True)
        axes[3,1].plot(t, dz);        axes[3,1].set_ylabel(r"$\dot{z}$");   axes[3,1].grid(True)
        axes[4,0].plot(t, f);         axes[4,0].set_ylabel(r"$f$");         axes[4,0].grid(True)
        axes[4,0].plot(t, np.zeros_like(t), "r--", label=r"$f=0$")
        axes[4,1].plot(t, phi);       axes[4,1].set_ylabel(r"$\phi$");      axes[4,1].grid(True)
        axes[4,1].plot(t,  np.pi/2 * np.ones_like(t), "r--")
        axes[4,1].plot(t, -np.pi/2 * np.ones_like(t), "r--")

        for ax in axes[-1]:
            ax.set_xlabel(r"time $t$")

        # Check boundary conditions
        print("=== Initial conditions ===")
        print(f"x(0)      = {x[0]:.4f}  (expected {x_0})")
        print(f"dx(0)     = {dx[0]:.4f}  (expected {dx_0})")
        print(f"y(0)      = {y[0]:.4f}  (expected {y_0})")
        print(f"dy(0)     = {dy[0]:.4f}  (expected {dy_0})")
        print(f"theta(0)  = {theta[0]:.4f}  (expected {theta_0:.4f})")
        print(f"dtheta(0) = {dtheta[0]:.4f}  (expected {dtheta_0})")
        print(f"z(0)      = {z[0]:.4f}  (expected {z_0})")
        print(f"dz(0)     = {dz[0]:.4f}  (expected {dz_0})")

        print("\n=== Final conditions ===")
        print(f"x(tf)      = {x[-1]:.4f}  (expected {x_tf})")
        print(f"dx(tf)     = {dx[-1]:.4f}  (expected {dx_tf})")
        print(f"y(tf)      = {y[-1]:.4f}  (expected {y_tf})")
        print(f"dy(tf)     = {dy[-1]:.4f}  (expected {dy_tf})")
        print(f"theta(tf)  = {theta[-1]:.4f}  (expected {theta_tf})")
        print(f"dtheta(tf) = {dtheta[-1]:.4f}  (expected {dtheta_tf})")
        print(f"z(tf)      = {z[-1]:.4f}  (expected {z_tf})")
        print(f"dz(tf)     = {dz[-1]:.4f}  (expected {dz_tf})")

        plt.tight_layout()
        return mo.center(fig)

    graphical_validation()
    return


@app.cell
def _(M, booster_anim, compute, g, l, mo, np, world):
    def animation_validation():
        x_0, dx_0      = 5.0,  0.0
        y_0, dy_0      = 20.0, -1.0
        theta_0        = -np.pi/8
        dtheta_0       = 0.0
        z_0, dz_0      = -M*g, 0.0

        x_tf, dx_tf    = 0.0,  0.0
        y_tf, dy_tf    = 2/3*l, 0.0
        theta_tf       = 0.0
        dtheta_tf      = 0.0
        z_tf, dz_tf    = -M*g, 0.0

        tf = 10.0

        fun = compute(
            x_0, dx_0, y_0, dy_0, theta_0, dtheta_0, z_0, dz_0,
            x_tf, dx_tf, y_tf, dy_tf, theta_tf, dtheta_tf, z_tf, dz_tf,
            tf,
        )

        def x(t):     return fun(t)[0]
        def y(t):     return fun(t)[2]
        def theta(t): return fun(t)[4]
        def f(t):     return fun(t)[8]
        def phi(t):   return fun(t)[9]

        return mo.Html(
            world(
                [-6, 6, -2, 22],
                booster_anim(x, y, theta, f, phi, T=tf)
            )
        ).center()

    animation_validation()
    return


if __name__ == "__main__":
    app.run()
