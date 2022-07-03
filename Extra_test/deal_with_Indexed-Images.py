# import torchvision.transforms as standard_transforms
# import numpy as np
# import json
# from PIL import Image
# import cv2

#########################################Image 读取#########################################

# 此图像称为索引图，由矩阵和对应的map组成
# label3 = Image.open('./test_img2/augsburg_000000_000000_rightImg8bit_prediction.png')
# label3 = np.array(label3).astype(np.int64)


#########################################Image 保存#########################################

# def fill_colormap(self):
#     palette = [128, 64, 128,
#                 244, 35, 232,
#                 70, 70, 70,
#                 102, 102, 156,
#                 190, 153, 153,
#                 153, 153, 153,
#                 250, 170, 30,
#                 220, 220, 0,
#                 107, 142, 35,
#                 152, 251, 152,
#                 70, 130, 180,
#                 220, 20, 60,
#                 255, 0, 0,
#                 0, 0, 142,
#                 0, 0, 70,
#                 0, 60, 100,
#                 0, 80, 100,
#                 0, 0, 230,
#                 119, 11, 32]
#     zero_pad = 256 * 3 - len(palette)
#     for i in range(zero_pad):
#         palette.append(0)
#     self.color_mapping = palette



# def colorize_mask(self, image_array):
#     """
#     Colorize the segmentation mask
#     """
#     new_mask = Image.fromarray(image_array.astype(np.uint8)).convert('P')
#     new_mask.putpalette(self.color_mapping)
#     return new_mask



# colorize_mask_fn = cfg.DATASET_INST.colorize_mask



# __C.DATASET.MEAN = [0.485, 0.456, 0.406]
# __C.DATASET.STD = [0.229, 0.224, 0.225]


# inv_mean = [-mean / std for mean, std in zip(cfg.DATASET.MEAN,
#                                             cfg.DATASET.STD)]
# inv_std = [1 / std for std in cfg.DATASET.STD]
# self.inv_normalize = standard_transforms.Normalize(
#     mean=inv_mean, std=inv_std
# )



# input_image = self.inv_normalize(input_image)
# input_image = input_image.cpu()
# input_image = standard_transforms.ToPILImage()(input_image)
# input_image = input_image.convert("RGB")
# input_image_fn = f'{img_name}_input.png'
# input_image.save(os.path.join(self.save_dir, input_image_fn))

# 索引图保存方法
# gt_fn = '{}_gt.png'.format(img_name)
# gt_pil = colorize_mask_fn(gt_image.cpu().numpy())
# gt_pil.save(os.path.join(self.save_dir, gt_fn))

# prediction_fn = '{}_prediction.png'.format(img_name)
# prediction_pil = colorize_mask_fn(prediction)
# prediction_pil.save(os.path.join(self.save_dir, prediction_fn))

# 彩图叠加方法
# prediction_pil = prediction_pil.convert('RGB')
# composited = Image.blend(input_image, prediction_pil, 0.4) #blend_img = img1*(1-alpha) + img2*alpha
# composited_fn = 'composited_{}.png'.format(img_name)
# composited_fn = os.path.join(self.save_dir, composited_fn)
# composited.save(composited_fn)