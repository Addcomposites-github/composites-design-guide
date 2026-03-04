import { useCallback, useState } from "react";
import { useDropzone } from "react-dropzone";
import { Upload, X, Image as ImageIcon } from "lucide-react";

interface PhotoUploadProps {
  onPhotoChange: (base64: string | null) => void;
}

export default function PhotoUpload({ onPhotoChange }: PhotoUploadProps) {
  const [preview, setPreview] = useState<string | null>(null);
  const [fileName, setFileName] = useState<string | null>(null);

  const onDrop = useCallback(
    (acceptedFiles: File[]) => {
      const file = acceptedFiles[0];
      if (!file) return;

      setFileName(file.name);

      const reader = new FileReader();
      reader.onload = () => {
        const result = reader.result as string;
        setPreview(result);

        // Extract base64 portion (remove the data:image/...;base64, prefix)
        const base64 = result.split(",")[1];
        onPhotoChange(base64);
      };
      reader.readAsDataURL(file);
    },
    [onPhotoChange]
  );

  const removePhoto = useCallback(() => {
    setPreview(null);
    setFileName(null);
    onPhotoChange(null);
  }, [onPhotoChange]);

  const { getRootProps, getInputProps, isDragActive } = useDropzone({
    onDrop,
    accept: {
      "image/jpeg": [".jpg", ".jpeg"],
      "image/png": [".png"],
      "image/webp": [".webp"],
    },
    maxFiles: 1,
    maxSize: 10 * 1024 * 1024, // 10 MB
  });

  if (preview) {
    return (
      <div className="relative overflow-hidden rounded-lg border border-secondary-200 dark:border-secondary-700">
        <img
          src={preview}
          alt="Uploaded part photo"
          className="h-56 w-full object-contain bg-secondary-50 dark:bg-secondary-800"
        />
        <div className="flex items-center justify-between bg-white px-3 py-2 dark:bg-secondary-900">
          <div className="flex items-center gap-2 text-sm text-secondary-600 dark:text-secondary-400">
            <ImageIcon size={16} />
            <span className="truncate max-w-[200px]">{fileName}</span>
          </div>
          <button
            type="button"
            onClick={removePhoto}
            className="flex items-center gap-1 rounded px-2 py-1 text-sm text-danger-500 transition-colors hover:bg-red-50 dark:hover:bg-red-900/20"
          >
            <X size={14} />
            Remove
          </button>
        </div>
      </div>
    );
  }

  return (
    <div
      {...getRootProps()}
      className={`flex cursor-pointer flex-col items-center justify-center rounded-lg border-2 border-dashed px-4 py-8 transition-colors ${
        isDragActive
          ? "border-primary-400 bg-primary-50 dark:border-primary-500 dark:bg-primary-900/20"
          : "border-secondary-300 bg-secondary-50 hover:border-primary-400 hover:bg-primary-50 dark:border-secondary-600 dark:bg-secondary-800 dark:hover:border-primary-500 dark:hover:bg-primary-900/20"
      }`}
    >
      <input {...getInputProps()} />
      <Upload
        size={32}
        className={`mb-2 ${
          isDragActive
            ? "text-primary-600 dark:text-primary-400"
            : "text-secondary-400 dark:text-secondary-500"
        }`}
      />
      {isDragActive ? (
        <p className="text-sm font-medium text-primary-700 dark:text-primary-300">
          Drop the image here
        </p>
      ) : (
        <>
          <p className="text-sm font-medium text-secondary-700 dark:text-secondary-300">
            Drag and drop a photo, or click to browse
          </p>
          <p className="mt-1 text-xs text-secondary-500 dark:text-secondary-400">
            JPG, PNG, or WebP up to 10 MB
          </p>
        </>
      )}
    </div>
  );
}
