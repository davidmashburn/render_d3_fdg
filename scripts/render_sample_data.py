import render_d3_fdg

from render_d3_fdg.render_d3_fdg import fdg, fdg_plus_images
from render_d3_fdg.sample_data import sample_nodes, sample_links

if __name__ == "__main__":
    # fdg(sample_nodes, sample_links, save_freq=60) # version that auto-DL's svgs
    # fdg_plus_images(sample_nodes, sample_links, save_freq=20) # version that auto-DL's svg's AND converts to pngs and animated gif
    # fdg_plus_images(sample_nodes, sample_links) # saves just the image of the final render
    vals = sorted({i[2] for i in sample_links})
    sample_links = [(i, j, vals.index(k) * 1.0 / len(vals)) for i, j, k in sample_links]
    fdg_plus_images(
        sample_nodes,
        sample_links,
        title="Shakespeare characters",
        # save_freq=None,
        html_filename="fdg_base.html.template",
    )  # disabled saving, best for testing

