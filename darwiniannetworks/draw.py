from matplotlib.pyplot import *


def draw_population(population,
                    radius_ratio=0.15, position=(0.5, 0.5),
                    facecolor="1.0", edgecolor="0.0", linestyle="solid",
                    combative_colors=[],
                    docile_colors=[],
                    trait_radius=0.04, trait_h_shift=0.1, trait_v_shift=0.1,
                    axes=None, show_drawings=True):
    # if no axes given
    if not axes:
        fig, ax = subplots()
    else:
        ax = axes

    # compute best population radius
    max_traits_size = max(
        [len(population.combative()), len(population.docile())])
    radius = radius_ratio * \
        (max_traits_size * (-0.25 * max_traits_size + 1.25))

    # draw population circle
    circle = Circle(position, radius, facecolor=facecolor,
                    edgecolor=edgecolor, linestyle=linestyle, zorder=2)
    ax.add_patch(circle)

    # draw traits
    draw_traits(population.combative(), -1,
                position, trait_h_shift, trait_v_shift, trait_radius,
                axes=ax)
    draw_traits(population.docile(), 1,
                position, trait_h_shift, trait_v_shift, trait_radius,
                axes=ax)

    # show drawing
    if show_drawings:
        axis('equal')
        axis('off')
        show()


def draw_traits(traits, left_right, population_position,
                trait_h_shift, trait_v_shift, trait_radius,
                combative_color="1.0", docile_color="0.0",
                fontsize=12, trait_text_color="0.0",
                edgecolor="0.0", axes=gca()):
    traits_color = combative_color
    if left_right == 1:
        traits_color = docile_color
        trait_text_color = "1.0"
    initial_gap = int(len(traits) / 2)
    for i in range(len(traits)):
        # draw trait's circle
        c_x = population_position[0] + left_right * trait_h_shift
        c_y = population_position[1] + (initial_gap - i) * trait_v_shift
        c = Circle(
            (c_x, c_y),
            trait_radius,
            facecolor=traits_color,
            edgecolor=edgecolor,
            zorder=3
        )
        axes.add_patch(c)
        # draw trait's text
        axes.text(c_x, c_y, traits[i], fontsize=fontsize,
                  horizontalalignment='center', verticalalignment='center',
                  color=trait_text_color)


def draw_dn(dn, axes=None, show_drawings=True, divisions=3,
            horizontal_shift=0.5, vertical_shift=-0.5,
            radius_ratio=0.5,
            facecolor="1.0", edgecolor="0.0", linestyle="dashed",):

    # if no axes given
    if not axes:
        fig, ax = subplots()

    # draw populations
    horizontal_counter = 0
    vertical_counter = 0
    total_rows = 1
    for pop in dn.populations:
        draw_population(pop,
                        position=(
                            horizontal_counter * horizontal_shift,
                            vertical_counter * vertical_shift),
                        axes=ax,
                        show_drawings=False)
        horizontal_counter += 1
        if (horizontal_counter % divisions) == 0:
            vertical_counter += 1
            horizontal_counter = 1
            total_rows += 1

    # draw dashed DN circle
    max_pop_size = max(total_rows, divisions)
    radius = radius_ratio * (max_pop_size * (-0.25 * max_pop_size + 1.25))
    position = (-total_rows * vertical_shift / 2 + 0.5 *
                vertical_shift,
                -divisions * horizontal_shift / 2 + horizontal_shift)
    circle = Circle(position, radius, facecolor=facecolor,
                    edgecolor=edgecolor, linestyle=linestyle,
                    zorder=1)
    ax.add_patch(circle)

    # show drawing
    if show_drawings:
        axis('equal')
        axis('off')
        show()
