#!/bin/bash

echo "🚀 Setting up pre-commit hooks for Massive DevOps..."

# Check if pre-commit is installed
if ! command -v pre-commit &> /dev/null; then
    echo "❌ pre-commit is not installed. Installing..."
    pip install pre-commit
else
    echo "✅ pre-commit is already installed"
fi

# Install pre-commit hooks
echo "📦 Installing pre-commit hooks..."
pre-commit install

# Install commit-msg hook for conventional commits
echo "📝 Installing commit-msg hook for conventional commits..."
pre-commit install --hook-type commit-msg

# Update hooks to latest versions
echo "🔄 Updating hooks to latest versions..."
pre-commit autoupdate

# Run pre-commit on all files
echo "🧹 Running pre-commit on all files..."
pre-commit run --all-files || true

echo "✅ Pre-commit setup complete!"
echo ""
echo "📋 Next steps:"
echo "1. Make sure your commits follow conventional commit format"
echo "2. Run 'pre-commit run --all-files' to check all files"
echo "3. Run 'pre-commit run <hook-name>' to run specific hooks"
echo ""
echo "🔗 Useful commands:"
echo "- pre-commit run --all-files    # Run on all files"
echo "- pre-commit run                # Run on staged files"
echo "- pre-commit autoupdate         # Update hooks"
echo "- git commit --no-verify        # Skip pre-commit (not recommended)"
