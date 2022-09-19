{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ef0efec0",
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "import cv2\n",
    "\n",
    "cv2.startWindowThread()\n",
    "cap = cv2.VideoCapture(0)\n",
    "\n",
    "while(True):\n",
    "    # reading the frame\n",
    "    ret, frame = cap.read()\n",
    "    # displaying the frame\n",
    "    cv2.imshow('frame',frame)\n",
    "    if cv2.waitKey(1) & 0xFF == ord('q'):\n",
    "        # breaking the loop if the user types q\n",
    "        # note that the video window must be highlighted!\n",
    "        break\n",
    "\n",
    "cap.release()\n",
    "cv2.destroyAllWindows()\n",
    "# the following is necessary on the mac,\n",
    "# maybe not on other platforms:\n",
    "cv2.waitKey(1)\n",
    "\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
