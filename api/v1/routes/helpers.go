package helpers

import (
	"crypto/rand"
	"encoding/hex"
	"errors"
	"strings"
	"time"
)

const (
	DefaultCurrency = "USD"
)

func GenerateTransactionID() (string, error) {
	b := make([]byte, 16)
	_, err := rand.Read(b)
	if err != nil {
		return "", err
	}
	return hex.EncodeToString(b), nil
}

func ValidateCurrency(currency string) bool {
	currency = strings.ToUpper(currency)
	supportedCurrencies := []string{"USD", "EUR", "GBP", "JPY"}
	for _, supported := range supportedCurrencies {
		if currency == supported {
			return true
		}
	}
	return false
}

func FormatAmount(amount float64, currency string) string {
	return strings.ToUpper(currency) + " " + formatDecimal(amount)
}

func formatDecimal(amount float64) string {
	return strings.TrimRight(strings.TrimRight(formatDecimal(amount), "0"), ".")
}

func ParseTimestamp(timestamp string) (time.Time, error) {
	return time.Parse(time.RFC3339, timestamp)
}

func ValidateTransactionAmount(amount float64) error {
	if amount <= 0 {
		return errors.New("amount must be greater than zero")
	}
	return nil
}