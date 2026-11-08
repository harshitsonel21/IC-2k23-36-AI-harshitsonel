# Grad-CAM implementation notes

Grad-CAM explains a CNN prediction by combining gradients flowing into a chosen convolutional layer with that layer's feature maps.

Typical steps:
1. Load a trained CNN and an input image.
2. Register forward and backward hooks on the target convolutional layer.
3. Run inference and select the class score to explain.
4. Backpropagate that score.
5. Globally average gradients over spatial dimensions to obtain channel weights.
6. Compute the weighted sum of feature maps, apply ReLU, normalize, and resize the heatmap.
7. Overlay the heatmap on the original image and interpret cautiously.

A meaningful Grad-CAM experiment requires a trained image model, a compatible target layer, and an image dataset. These are not supplied in the lab handout, so no fabricated heatmap is included.
